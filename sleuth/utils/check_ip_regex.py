import re

import sleuth.constants as constants

def check_ip_regex(ip: str) -> bool:
    """ Checks the ip regex if it's banned and if it's a valid ip format """
    # Check if the ip format is valid or
    if not re.match(constants.VALID_IP_REGEX, ip) is not None:
        return False

    # Check if the ip localhost or 127.0.0.1
    for regex in constants.BANNED_IPs_REGEX:
        return not re.match(regex, ip) is not None

    return True
