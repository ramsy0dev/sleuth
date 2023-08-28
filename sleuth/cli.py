import os
import sys
import typer

from rich import print
from rich.prompt import Prompt

import sleuth.constants as constants

from sleuth.messages import (
    errors,
    info
)

from sleuth.src.result_table.table import result_table
from sleuth.src.config_data import save_sleuth_config
from sleuth.src.database.database_handler import DatabaseHandler
from sleuth.src.database.database_connection import DatabaseConnection

# Utils
from sleuth.utils.clock import clock
from sleuth.utils.date import date
from sleuth.utils.check_ip import check_ip
from sleuth.utils.print_config import print_config
from sleuth.utils.check_config import check_config
from sleuth.utils.check_ip_regex import check_ip_regex
from sleuth.utils.create_database_url import create_database_url
from sleuth.utils.generate_uid import generate_uuid

# Models
from sleuth.src.models.sleuth_config_model import SleuthConfig
from sleuth.src.models.targeted_ip_model import TargetedIP

# Services
from sleuth.src.services.vpnapi import vpnapi
from sleuth.src.services.ip_api import ip_api
from sleuth.src.services.nmap import nmap_scanner

# Init the cli
cli = typer.Typer()

@cli.command()
def version():
    """ Sleuth's current version"""
    print(f"[bold cyan]Version [bold white]{constants.VERSION}")

@cli.command()
def setup():
    """ Setup Sleuth's database to use """
    skip_postgresql_questions = False

    # Checking for existing configuration file
    if check_config():
        try:
            sleuth_config = SleuthConfig()
        except Exception as error:
            sys.exit(1)

        is_to_reset_config_file = Prompt.ask(
            f"{clock()}[bold yellow] \[ ? ] [bold white]A config file already exists at [bold cyan]`{constants.SLEUTH_CONFIG_PATH}`[bold white]. Would like to reset that config file or exit",
            choices=["reset", "exit"],
            show_choices=True,
            default="exit",
            show_default=True
        )
        if is_to_reset_config_file == "exit":
            sys.exit(0)

        pass

    sleuth_config = {
        "enable_database_save": None,
        "vpn_api_key": None,
        "database_type": None,
        "sqlite_file_path": None,
        "username": None,
        "password": None,
        "host": None,
        "port": None,
        "database_name": None
    }

    vpn_api_key = Prompt.ask(f"{clock()}[bold green] \[ + ] [bold white]Enter your [bold green]vpnapi.io[bold white]'s API [bold red]key[bold white]")

    if vpn_api_key == "":
        print(f"{clock()}[bold yellow]     \__[ ! ] [bold greeb]vpnapi.io[bold white]'s API [bold red]won't[bold white] be used, because no API [bold red]key was provided.")
    else:
        sleuth_config["vpn_api_key"] = vpn_api_key

    enable_database_save = Prompt.ask(
        f"{clock()}[bold green] \[ + ] [bold white]Would you like to save your results in a [bold green]database[bold white]?",
        choices=[
            "yes",
            "no"
        ],
        show_choices=True,
        default="yes"
    )
    if enable_database_save == "no":
        sleuth_config["enable_database_save"] = False
        save_sleuth_config(
            sleuth_config_data=sleuth_config
        )
        print(f"{clock()}{info.CONFIG_SAVED(sleuth_config_path=constants.SLEUTH_CONFIG_PATH)}\n{clock()}[bold green]      \__[ + ] [bold white]Saved config data:")
        print_config(config=sleuth_config)

        sys.exit(0)

    database_type = Prompt.ask(
        f"{clock()}[bold green] \[ + ] [bold white]What is your [bold green]database `type`[bold white]?",
        choices=[
            "postgresql",
            "sqlite"
        ],
        show_choices=True,
        default="sqlite"
    )
    if database_type == "sqlite":
        sleuth_config["enable_database_save"] = True
        sleuth_config["database_type"] = database_type

        sqlite_file_path = Prompt.ask(
            f"{clock()}[bold green] \[ + ] [bold white]What is your [bold green]sqlite database path[bold white]? [bold yellow](leave this blank to generate it for you)[bold white]"
        )
        if sqlite_file_path == "":
            sleuth_config["sqlite_file_path"] = constants.DEFAULT_SQLITE_PATH
            os.system(f"touch {constants.DEFAULT_SQLITE_PATH}")

        save_sleuth_config(
            sleuth_config_data=sleuth_config
        )
        print(f"{clock()}{info.CONFIG_SAVED(sleuth_config_path=constants.SLEUTH_CONFIG_PATH)}\n{clock()}[bold green]      \__[ - ] [bold white]Saved config data:")
        print_config(config=sleuth_config)

        skip_postgresql_questions = True

    if not skip_postgresql_questions:
        username = Prompt.ask(f"{clock()}[bold green] \[ + ] [bold white]What is your [bold green]database `username`[bold white]?")
        password = Prompt.ask(
            f"{clock()} [bold green] \[ + ] [bold white]What is your [bold green]database `password`[bold white]?", password=True
        )
        host = Prompt.ask(f"{clock()}[bold green] \[ + ] [bold white]What is your [bold green]database `host`[bold white]?")
        port = Prompt.ask(f"{clock()}[bold green] \[ + ] [bold white]What is your [bold green]database `port`[bold white]?")
        database_name = Prompt.ask(f"{clock()}[bold green] \[ + ] [bold white]What is your [bold green]`database_name`[bold white]?")

        sleuth_config["enable_database_save"] = True
        sleuth_config["database_type"] = database_type
        sleuth_config["username"] = username
        sleuth_config["password"] = password
        sleuth_config["host"] = host
        sleuth_config["port"] = port
        sleuth_config["database_name"] = database_name

        save_sleuth_config(
            sleuth_config_data=sleuth_config
        )
        print(f"{clock()}{info.CONFIG_SAVED(sleuth_config_path=constants.SLEUTH_CONFIG_PATH)}\n{clock()}[bold green]      \__[ + ] [bold white]Saved config data:")
        print_config(config=sleuth_config)

    # Setting up the database (tables and columns)
    sleuth_config = SleuthConfig() # Getting the new "saved" config

    database_url = create_database_url(
        sleuth_config=sleuth_config
    )

    print(r"{}{}".format(clock(), info.CONNECTING_TO_DATABASE(database_type=sleuth_config.database_type,database_url=database_url)), end="")

    try:
        database_connection = DatabaseConnection(
            database_url=database_url
        )
    except Exception as error:
        print("[bold red] FAILD")
        print(f"{clock()}{errors.FAILD_TO_CONNECT_TO_THE_DATABASE(database_type=database_type,database_url=database_url,error=error)}")
        sys.exit(1)

    print("[bold green] DONE")

    database_handler = DatabaseHandler(
        database_connection=database_connection,
        database_type=sleuth_config.database_type
    )

    print(f"{clock()}{info.SETTING_UP_DATABASE_TABLES}")

    database_handler.setup_tables()

    print(f"{clock()}{info.DATABASE_SETUP_IS_DONE}")

@cli.command()
def track(ip: str):
    """ Tracks a given IP address and returns info about it """
    # Check the Sleuth's config
    if not check_config():
        print(errors.NO_CONFIG_WAS_FOUND)
        sys.exit(1)

    # Connecting to the database
    sleuth_config = SleuthConfig()
    database_connection = None
    database_handler = None

    if sleuth_config.enable_database_save:
        database_url = create_database_url(
            sleuth_config=sleuth_config
        )
        database_connection = DatabaseConnection(
            database_url=database_url
        )
        database_handler = DatabaseHandler(
            database_connection=database_connection,
            database_type=sleuth_config.database_type
        )

        print(f"{clock()}{info.CONNECTED_TO_DATABASE(database_type=sleuth_config.database_type)}")

    # Check `ip`
    print(r"{}{}".format(clock(), info.CHECKING_IP_REGEX(ip=ip)), end="")

    if not check_ip_regex(ip=ip):
        print("[bold red] FAILD")
        print(f"{clock()}{errors.IP_REGEX_ERROR(ip=ip)}")
        sys.exit(1)

    print("[bold green] DONE")

    # Check if the `ip` exists in the database
    if database_handler.is_target_ip_exists(ip=ip):
        is_to_continue = Prompt.ask(
            f"{clock()}[bold green] \[ + ] [bold white]Target [bold red]IP:[bold green]`{ip}`[bold white] already exists in the [bold green]database[bold white]. Do you want to run [bold green]search[bold white] instead?",
            choices=["yes", "no"],
            default="yes",
            show_choices=True,
            show_default=True
        )

        if is_to_continue == "yes":
            print(f"{clock()}{info.RUN_THE_SEARCH_COMMAND(ip=ip)}")
            sys.exit()

    # Check if the `ip/host` is alive
    print(r"{}{}".format(clock(), info.CHECKING_IS_IP_RESPONSIVE(ip=ip)), end="")

    if not check_ip(ip=ip):
        print("[bold red] FAILD")
        print(f"{clock()}{errors.IP_IS_NOT_ALIVE(ip=ip)}")
        sys.exit(1)

    print("[bold green] DONE")

    targeted_ip = TargetedIP()

    targeted_ip.ip_uid  =    generate_uuid(data=ip)
    targeted_ip.ip      =    ip

    if sleuth_config.vpn_api_key == None:
        print(f"{clock()}{info.SKIPPING_VPN_API_SERVICE}")
    else:
        print(r"{}{}".format(clock(), info.RUNNING_VPNAPI(ip=ip)), end="")

        vpnapi_result = vpnapi(
            ip=ip,
            api_key=sleuth_config.vpn_api_key
        )
        associated_with = []

        for i in vpnapi_result:
            if vpnapi_result[i] == True:
                associated_with.append(i)
        if len(associated_with) > 0:
            targeted_ip.is_vpn      =   vpnapi_result["vpn"]
            targeted_ip.is_proxy    =   vpnapi_result["proxy"]
            targeted_ip.is_tor      =   vpnapi_result["tor"]
            targeted_ip.is_relay    =   vpnapi_result["relay"]

            print(f"{clock()}[bold yellow]     \__[ ! ] [bold red]IP:[bold green]`{ip}`[bold white] is associated with [bold yellow]{', '.join(associated_with)}")
        else:
            print("[bold green] DONE")

    save_to_database = sleuth_config.enable_database_save

    uid = ip_api(
        ip=ip,
        database_handler=database_handler,
        save_to_database=save_to_database
    )
    targeted_ip.ip_api_results_uid = uid

    # Running nmap scan
    nmap_services_uids = nmap_scanner(
        ip=ip,
        save_to_database=save_to_database,
        database_handler=database_handler
    )

    if not save_to_database:
        targeted_ip.nmap_services_uids = None
    elif nmap_services_uids != []:
        targeted_ip.nmap_services_uids = f"[{', '.join(nmap_services_uids)}]"
    else:
        targeted_ip.nmap_services_uids = nmap_services_uids

    targeted_ip.created_at = date()

    print(r"{}{}".format(clock(), info.SAVING_TARGETED_IP_INFO(ip=ip)), end="")
    database_handler.save_targeted_ip_data(targeted_ip)

    print("[bold green] DONE")

@cli.command()
def search(ip: str):
    """ Search for a target IP in the database """
    # Check the Sleuth's config
    if not check_config():
        print(f"{clock()}{errors.NO_CONFIG_WAS_FOUND}")
        sys.exit(1)

    # Connecting to the database
    sleuth_config = SleuthConfig()
    database_connection = None
    database_handler = None

    if not sleuth_config.enable_database_save:
        print(f"{clock()}{errors.NO_DATABASE_WAS_SETUP_TO_USE_SEARCH_COMMAND}")
        sys.exit(1)

    database_url = create_database_url(
        sleuth_config=sleuth_config
    )
    database_connection = DatabaseConnection(
        database_url=database_url
    )
    database_handler = DatabaseHandler(
        database_connection=database_connection,
        database_type=sleuth_config.database_type
    )

    print(f"{clock()}{info.CONNECTED_TO_DATABASE(database_type=sleuth_config.database_type)}")

    # Check `ip`
    print(r"{}{}".format(clock(), info.CHECKING_IP_REGEX(ip=ip)), end="")

    if not check_ip_regex(ip=ip):
        print("[bold red] FAILD")
        print(f"{clock()}{errors.IP_REGEX_ERROR(ip=ip)}")
        sys.exit(1)

    print("[bold green] DONE")

    # Check if the target ip exits in the databasse
    if not database_handler.is_target_ip_exists(ip=ip):
        print(f"{clock()}{errors.TARGET_IP_DOESNT_EXISTS_IN_THE_DATABASE(ip=ip)}")
        sys.exit(1)

    # Retrive data about the target ip from the database
    print(r"{}{}".format(clock(), info.FETCHING_DATA_FROM_THE_DATABASE(ip=ip)), end="")

    target_ip = database_handler.fetch_target_ip_data(ip=ip)

    nmap_services = []

    for nmap_service_uid in target_ip.nmap_services_uids:
        nmap_service = database_handler.fetch_nmap_services(nmap_service_uid=nmap_service_uid)

        nmap_services.append(nmap_service)

    ip_api_result = database_handler.fetch_ip_api_result(ip_api_results_uid=target_ip.ip_api_results_uid)

    print("[bold green] DONE")

    print(f"{clock()}{info.TARGET_IP_INFO(ip=ip)}")

    columns = [column for column in target_ip.export_dict()]
    rows = [[target_ip.export_dict()[row] for row in target_ip.export_dict()], ]

    result_table(
        title="Target IP basic info",
        columns=columns,
        rows=rows
    )

    print(f"{clock()}{info.IP_API_RESULTS}")

    columns = [column for column in ip_api_result.export_dict()]
    rows = [[str(row) for row in ip_api_result.export_tuple()[1:]],]

    # Deviding the tables because the results will not all be shown
    table_length = len(columns)
    lines = 4
    columns_for_tables = int(table_length/lines)

    last_column_number = 0
    columns_number = columns_for_tables

    for i in range(lines+1):
        title = "ipapi.com resutls" if i == 0 else ""

        if i == lines:
            _columns = columns[last_column_number:]
            _rows = [rows[0][last_column_number:], ]
        else:
            _columns = columns[last_column_number:columns_number]
            _rows = [rows[0][last_column_number:columns_number], ]

        result_table(
            title=title,
            columns=_columns,
            rows=_rows
        )

        last_column_number = columns_number
        columns_number += columns_for_tables

    print(f"{clock()}{info.NMAP_RESULTS}")

    columns = [column for column in nmap_services[0].export_dict()]
    rows = [row.export_tuple()[1:] for row in nmap_services]

    result_table(
        title="Nmap results",
        columns=columns,
        rows=rows
    )
