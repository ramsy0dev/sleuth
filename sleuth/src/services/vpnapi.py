import requests

from random_user_agent.user_agent import UserAgent

import sleuth.constants as constants

def vpnapi(ip: str, api_key: str) -> dict:
    """ Checks if the IP is associated to a VPN, PROXY, TOR NETWORK, RELAY. """
    result = None
    user_agent = UserAgent()

    headers = {
        "User-Agent": user_agent.get_random_user_agent()
    }
    vpnapi_response = requests.get(
        constants.VPN_API(
            ip=ip,
            api_key=api_key
        ),
        headers=headers
    )

    vpnapi_response = vpnapi_response.json()

    result = vpnapi_response["security"]
    
    return result
