
class ServiceVersion(object):
    """ The service version ouputed form the nmap scan model """
    service: dict
    port: str
    protocol: str
    state: str
    version: str
    reason: str
    reason_ttl: str
    cpe: list[dict]

    def set_fields(self, ip: str, nmap_result: dict) -> None:
        """ Sets the values of the fields to their corresonding variable """
        if "product" not in [keys for keys in nmap_result["service"]]:
            self.service = nmap_result["service"]["name"]
        else:
            self.service = f"{nmap_result['service']['name']} / {nmap_result['service']['product']}"


        self.port        = nmap_result["portid"]
        self.protocol    = nmap_result["protocol"]
        self.state       = nmap_result["state"]

        if "version" not in [keys for keys in nmap_result["service"]] and "extrainfo" in [keys for keys in nmap_result["service"]] and len(nmap_result["cpe"]) != 0:
            self.version = nmap_result["cpe"][0]["cpe"].split(":")[-1]
        elif "version" not in [keys for keys in nmap_result["service"]] and "extrainfo" in [keys for keys in nmap_result["service"]]:
            self.version = nmap_result["service"]["extrainfo"]
        elif "version" in [keys for keys in nmap_result["service"]]:
            self.version = nmap_result["service"]["version"]
        else:
            self.version = "Null"

        self.reason      = nmap_result["reason"]
        self.reason_ttl  = nmap_result["reason_ttl"]

        if len(nmap_result["cpe"]) == 0:
            self.cpe = "Null"
        else:
            self.cpe = nmap_result["cpe"][0]["cpe"]

    def export_tuple(self) -> tuple:
        """ Returns the data in a tuple format to save it in the database """
        return (
            self.service,
            self.port,
            self.protocol,
            self.state,
            self.version,
            self.reason,
            self.reason_ttl,
            self.cpe
        )

    def export_dict(self) -> dict:
        """ Returns the data in a json format to print it out to the stdout """
        return {
            "service": self.service,
            "port": self.port,
            "protocol": self.protocol,
            "state": self.state,
            "version": self.version,
            "reason": self.reason,
            "reason_ttl": self.reason_ttl,
            "cpe": self.cpe
        }
