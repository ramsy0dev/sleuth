import os
import sys
import yaml

import sleuth.constants as constants

from sleuth.messages import errors
from sleuth.utils.check_config import check_config

def sleuth_config() -> dict:
    """ Returns a dict representing the config for Sleuth """
    with open(constants.SLEUTH_CONFIG_PATH, "r") as sleuth_config_data:
        sleuth_config_data = yaml.safe_load(sleuth_config_data)

    try:
        database = sleuth_config_data["database"]

        sleuth_config_data = {
            "enable_database_save": sleuth_config_data["enable_database_save"],
            "vpn_api_key": sleuth_config_data["vpn_api_key"],
            "database_type": database[0]["database_type"],
            "sqlite_file_path": database[1]["sqlite_file_path"],
            "username": database[2]["username"],
            "password": database[3]["password"],
            "host": database[4]["host"],
            "port": database[5]["port"],
            "database_name": database[6]["database_name"]
        }
    except:
        print(errors.CONFIG_FILE_IS_CORRUPTED)
        sys.exit()

    return sleuth_config_data

def save_sleuth_config(sleuth_config_data: dict) -> None:
    """ Saves the sleuth config data """
    sleuth_config_data = constants.SLEUTH_CONFIG(
        enable_database_save=sleuth_config_data["enable_database_save"],
        vpn_api_key=sleuth_config_data["vpn_api_key"],
        database_type = sleuth_config_data["database_type"],
        sqlite_file_path = sleuth_config_data["sqlite_file_path"],
        username = sleuth_config_data["username"],
        password = sleuth_config_data["password"],
        host = sleuth_config_data["host"],
        port = sleuth_config_data["port"],
        database_name = sleuth_config_data["database_name"]
    )

    if not check_config():
        os.makedirs(f"{'/'.join(constants.SLEUTH_CONFIG_PATH.split('/')[:-1])}", exist_ok=True)

    with open(constants.SLEUTH_CONFIG_PATH, "w") as save_config:
        save_config.write(sleuth_config_data)
