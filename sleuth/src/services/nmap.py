import sys
import nmap3

from rich import print
from rich.prompt import Prompt

from sleuth.messages import (
    errors,
    info
)
from sleuth.src.result_table.table import result_table
from sleuth.src.database.database_handler import DatabaseHandler

# Utils
from sleuth.utils.clock import clock

# Models
from sleuth.src.models.service_version_model import ServiceVersion
from sleuth.src.models.os_info_model import OSInfo

def nmap_scanner(ip: str, save_to_database: bool, database_handler: DatabaseHandler, enable_os_detection: bool | None = False) -> None:
    """ Preformes an nmap scan on the targeted `ip` """
    nmap = nmap3.Nmap()
    services_version = []
    # os_info = OSInfo()

    print(r"{}{}".format(clock(), info.RUNNING_NMAP_SCAN), end="")

    try:
        scan_results = nmap.nmap_version_detection(ip)

        for service in scan_results[ip]["ports"]:
            service_version = ServiceVersion()

            service_version.set_fields(
                ip=ip,
                nmap_result=service
            )

            services_version.append(service_version)
            print("[bold green] DONE") # Nmap scan was successfully ran
    except Exception as error:
        print("[bold red] FAILD")
        print(f"{clock()}{errors.NMAP_SCAN_FAILD(ip=ip, error=error)}")

        is_to_continue = Prompt.ask(
            "Do you want to continue?",
            choices=["yes","no"],
            default="no",
            show_choices=True,
            show_default=True
        )

        if not is_to_continue:
            sys.exit()

    # if enable_os_detection:
    #     os_detection_results = nmap.nmap_os_detection(ip)

    #     os_info.set_fields(
    #         ip=ip,
    #         nmap_resulte=os_detection_results
    #     )

    # Scan result
    columns = [
        "service",
        "port",
        "protocol",
        "state",
        "version",
        "reason",
        "reason TTL",
        "cpe"
    ]
    rows = list()

    for service in services_version:
        row = [*service.export_tuple()]

        rows.append(row)

    result_table(
        title="Nmap scan results",
        columns=columns,
        rows=rows
    )

    # Save data to the database in case of `save_to_database`
    if not save_to_database:
        return

    if len(services_version) == 0:
        return []

    print(r"{}{}".format(clock(), info.SAVING_NMAP_SCAN_RESULTS), end="")
    nmap_services_uuids = database_handler.save_nmap_scan_results(
        nmap_services=services_version
    )

    print("[bold green] DONE")

    return nmap_services_uuids
