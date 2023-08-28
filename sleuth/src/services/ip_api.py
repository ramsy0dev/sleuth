import requests

from rich import print
from random_user_agent.user_agent import UserAgent

import sleuth.constants as constants

from sleuth.messages import info
from sleuth.src.result_table.table import result_table
from sleuth.src.database.database_handler import DatabaseHandler

# Utils
from sleuth.utils.generate_uid import generate_uuid
from sleuth.utils.clock import clock

# Models
from sleuth.src.models.ip_api_model import IPAPI

def ip_api(ip: str, database_handler: DatabaseHandler, save_to_database: bool) -> str:
    """ Gather information about the `IP` """
    IP_Api = IPAPI()
    IP_Api.ip_api_results_uid = generate_uuid(data=ip)

    print(r"{}{}".format(clock(), info.RUNNING_IP_API(ip=ip)), end="")

    user_agent = UserAgent()
    headers = {
        "User-Agent": user_agent.get_random_user_agent()
    }
    ip_api_response = requests.get(
        constants.IP_API(ip=ip),
        headers=headers
    )

    ip_api_response = ip_api_response.json()
    IP_Api.set_fields(
        api_response=ip_api_response
    )

    print("[bold green] DONE")

    columns = [column for column in IP_Api.export_dict()]
    rows = [[str(row) for row in IP_Api.export_tuple()[1:]],]

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

    if not save_to_database:
        return

    print(r"{}{}".format(clock(), info.SAVING_IP_API_RESULTS), end="")
    database_handler.save_ip_api_results(ip_api=IP_Api)

    print("[bold green] DONE")

    return IP_Api.ip_api_results_uid
