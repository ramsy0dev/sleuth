class IPAPI(object):
    """ IPAPI model """
    ip_api_results_uid: str
    status: str
    continent: str
    continentCode: str
    country: str
    countryCode: str
    region: str
    regionName: str
    city: str
    district: str
    zip: str
    lat: float
    lon: float
    timezone: str
    offset: str
    currency: str
    isp: str
    org: str
    as_: str
    asname: str
    reverse: str
    mobile: bool
    proxy: bool
    hosting: bool
    query: str

    def set_fields(self, api_response: dict) -> None:
        """ Sets the api response for each field to the corresponding variable """
        for field in self.__annotations__:
            if field == "as_":
                setattr(self, "as_", api_response.get("as", None))
            elif field =="ip_api_results_uid":
                continue
            else:
                setattr(self, field, api_response.get(field, None))

    def export_dict(self) -> dict:
        """ Returns the attributes as dict """
        return {
            "status": self.status,
            "continent": self.continent,
            "continentCode": self.continentCode,
            "country": self.country,
            "countryCode": self.countryCode,
            "region": self.region,
            "regionName": self.regionName,
            "city": self.city,
            "district": self.district,
            "zip": self.zip,
            "lat": self.lat,
            "lon": self.lon,
            "timezone": self.timezone,
            "offset": self.offset,
            "currency": self.currency,
            "isp": self.isp,
            "org": self.org,
            "as": self.as_,
            "asname": self.asname,
            "reverse": self.reverse,
            "mobile": self.mobile,
            "proxy": self.proxy,
            "hosting": self.hosting,
            "query": self.query
        }

    def export_tuple(self) -> tuple:
        """ Returns the attributes as tuple """
        return (
            self.ip_api_results_uid,
            self.status,
            self.continent,
            self.continentCode,
            self.country,
            self.countryCode,
            self.region,
            self.regionName,
            self.city,
            self.district,
            self.zip,
            self.lat,
            self.lon,
            self.timezone,
            self.offset,
            self.currency,
            self.isp,
            self.org,
            self.as_,
            self.asname,
            self.reverse,
            self.mobile,
            self.proxy,
            self.hosting,
            self.query
        )
