import datetime

class TargetedIP (object):
    """ Targeted ip model """
    ip_uid: str
    ip: str
    is_vpn: bool | None = False
    is_proxy: bool | None = False
    is_tor: bool | None = False
    is_relay: bool | None = False
    nmap_services_uids: str
    ip_api_results_uid: str
    created_at: datetime.date

    def export_tuple(self) -> None:
        """ Exports the variables values in a tuple format """
        return (
            self.ip_uid,
            self.ip,
            self.is_vpn,
            self.is_proxy,
            self.is_tor,
            self.is_relay,
            self.nmap_services_uids,
            self.ip_api_results_uid,
            self.created_at
        )

    def export_dict(self) -> dict:
        """ Exports the variables values in a tuple format """
        return {
            "ip": self.ip,
            "is_vpn": self.is_vpn,
            "is_proxy": self.is_proxy,
            "is_tor": self.is_tor,
            "is_relay": self.is_relay,
            "created_at": self.created_at
        }
