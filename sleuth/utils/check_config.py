import os
import sleuth.constants as constants

def check_config() -> bool:
    """ Checks if Sleuth's config exists or not """
    return os.path.exists(constants.SLEUTH_CONFIG_PATH)
