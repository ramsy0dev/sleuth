from sleuth.src.config_data import sleuth_config

class SleuthConfig:
    """ Sleuth's config model """
    enable_database_save: bool
    vpn_api_key: str
    database_type: str
    sqlite_file_path: str
    username: str
    password: str
    host: str
    port: int
    database_name: str

    def __init__(self) -> None:
        sleuth_config_data = sleuth_config()

        for field in self.__annotations__:
            setattr(self, field, sleuth_config_data.get(field, None))
