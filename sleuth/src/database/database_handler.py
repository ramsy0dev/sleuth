from rich import print
from sqlalchemy import inspect, text

import sleuth.src.database.sqls.sql_commands as sql_commands

from sleuth.messages import info
from sleuth.src.database.database_connection import DatabaseConnection

# Utils
from sleuth.utils.clock import clock
from sleuth.utils.date import date
from sleuth.utils.generate_uid import generate_uuid

# Models
from sleuth.src.models.ip_api_model import IPAPI
from sleuth.src.models.targeted_ip_model import TargetedIP
from sleuth.src.models.service_version_model import ServiceVersion

class DatabaseHandler:
    """ Database handler class """
    def __init__(self, database_connection: DatabaseConnection, database_type: str) -> None:
        self.database_connection = database_connection
        self.database_engine = self.database_connection.engine
        self.database_session = self.database_connection.Session()
        self.database_type = database_type
        self.database_session.expire_on_commit = False

    def setup_tables(self) -> None:
        """ Setup all the needed tables in the database """
        inspector = inspect(self.database_engine)
        if self.database_type == "sqlite":
            tables = {
                "targeted_ips": sql_commands.TARGETED_IPS_TABLE_SQLITE,
                "ip_api_results": sql_commands.IP_API_TABLE_SQLITE,
                "nmap_services": sql_commands.NMAP_SERVICES_TABLE_SQLITE
            }
        else:
            tables = {
                "targeted_ips": sql_commands.TARGETED_IPS_TABLE_POSTGRESQL,
                "ip_api_results": sql_commands.IP_API_TABLE_POSTGRESQL,
                "nmap_services": sql_commands.NMAP_SERVICES_TABLE_POSTGRESQL
            }

        created_tables = inspector.get_table_names()

        for table in tables:
            if table not in created_tables:
                self.database_session.execute(tables[table])
                self.database_session.commit()

        print(f"{clock()}{info.TABLES_CREATED(tables_name=inspector.get_table_names())}")

    def save_targeted_ip_data(self, targeted_ip: TargetedIP) -> None:
        """ Saves the targeted ip gathered info in the database """
        sql = text("INSERT INTO targeted_ips VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % targeted_ip.export_tuple())

        self.database_session.execute(sql)
        self.database_session.commit()

    def save_nmap_scan_results(self, nmap_services: list[ServiceVersion]) -> list[str]:
        """ Saves the nmap services resulted from the namp scan into the database """
        uuids = []

        for service_version in nmap_services:
            data = service_version.export_tuple()
            uuid = generate_uuid(data=''.join(data))
            created_at = date()

            sql = text("INSERT INTO nmap_services VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (uuid, *service_version.export_tuple(), created_at))

            self.database_session.execute(sql)
            self.database_session.commit()

            uuids.append(uuid)

        return uuids

    def save_ip_api_results(self, ip_api: IPAPI) -> None:
        """ Saves the ip_api results into the database """
        created_at = date()
        sql = text("INSERT INTO ip_api_results VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (*ip_api.export_tuple(), created_at))

        self.database_session.execute(sql)
        self.database_session.commit()

    def fetch_target_ip_data(self, ip: str) -> TargetedIP:
        """ Fetchs the target `ip` data from the `targeted_ips` table """
        sql = text("SELECT * FROM targeted_ips WHERE ip = '%s'" % (ip, ))

        target_ip_data = self.database_session.execute(sql).fetchone()

        target_ip = TargetedIP()

        target_ip.ip_uid                =       target_ip_data[0]
        target_ip.ip                    =       target_ip_data[1]
        target_ip.is_vpn                =       target_ip_data[2]
        target_ip.is_proxy              =       target_ip_data[3]
        target_ip.is_tor                =       target_ip_data[4]
        target_ip.is_relay              =       target_ip_data[5]
        target_ip.nmap_services_uids    =       target_ip_data[6].replace("[", "").replace("]", "").split(", ")
        target_ip.ip_api_results_uid    =       target_ip_data[7]
        target_ip.created_at            =       target_ip_data[8]

        return target_ip

    def fetch_nmap_services(self, nmap_service_uid: str) -> ServiceVersion:
        """ Fetchs a service detect by nmap that is saved in the `nmap_services` table """
        sql = text("SELECT * FROM nmap_services WHERE nmap_service_uid = '%s'" % (nmap_service_uid, ))

        nmap_service_data = self.database_session.execute(sql).fetchone()

        nmap_service = ServiceVersion()

        nmap_service.service        =   nmap_service_data[0]
        nmap_service.port           =   nmap_service_data[1]
        nmap_service.protocol       =   nmap_service_data[2]
        nmap_service.state          =   nmap_service_data[3]
        nmap_service.version        =   nmap_service_data[4]
        nmap_service.reason         =   nmap_service_data[5]
        nmap_service.reason_ttl     =   nmap_service_data[6]
        nmap_service.cpe            =   nmap_service_data[7]

        return nmap_service

    def fetch_ip_api_result(self, ip_api_results_uid: str) -> IPAPI:
        """ Fetchs the `ipapi.com` results from `ip_api_results` table """
        sql = text("SELECT * FROM ip_api_results WHERE ip_api_results_uid = '%s'" % (ip_api_results_uid, ))

        ip_api_results = self.database_session.execute(sql).fetchone()

        ip_api = IPAPI()

        ip_api.ip_api_results_uid       =       ip_api_results[0]
        ip_api.status                   =       ip_api_results[1]
        ip_api.continent                =       ip_api_results[2]
        ip_api.continentCode            =       ip_api_results[3]
        ip_api.country                  =       ip_api_results[4]
        ip_api.countryCode              =       ip_api_results[5]
        ip_api.region                   =       ip_api_results[6]
        ip_api.regionName               =       ip_api_results[7]
        ip_api.city                     =       ip_api_results[8]
        ip_api.district                 =       ip_api_results[9]
        ip_api.zip                      =       ip_api_results[10]
        ip_api.lat                      =       ip_api_results[11]
        ip_api.lon                      =       ip_api_results[12]
        ip_api.timezone                 =       ip_api_results[13]
        ip_api.offset                   =       ip_api_results[14]
        ip_api.currency                 =       ip_api_results[15]
        ip_api.isp                      =       ip_api_results[16]
        ip_api.org                      =       ip_api_results[17]
        ip_api.as_                      =       ip_api_results[18]
        ip_api.asname                   =       ip_api_results[19]
        ip_api.reverse                  =       ip_api_results[20]
        ip_api.mobile                   =       ip_api_results[21]
        ip_api.proxy                    =       ip_api_results[22]
        ip_api.hosting                  =       ip_api_results[23]
        ip_api.query                    =       ip_api_results[24]

        return ip_api

    def is_target_ip_exists(self, ip: str) -> bool:
        """ Checks if a target `ip` exists in the `targeted_ips` table"""
        sql = text("SELECT * FROM targeted_ips WHERE ip = '%s'" % (ip, ))

        row = self.database_session.execute(sql).fetchall()

        return not len(row) == 0 # True if the row containes columns values, otherwise False
