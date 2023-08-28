from sleuth.src.models.sleuth_config_model import SleuthConfig

def create_database_url(
    sleuth_config: SleuthConfig
) -> str:
    """ Creates a database url of the database info """
    database_url = None

    if sleuth_config.database_type == "sqlite":
        database_url = f"sqlite:///{sleuth_config.sqlite_file_path}"
    elif sleuth_config.database_type == "postgresql":
        database_url = f"postgresql://{sleuth_config.username}:{sleuth_config.password}@{sleuth_config.host}:{sleuth_config.port}/{sleuth_config.database_name}"

    return database_url
