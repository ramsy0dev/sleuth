class OSInfo(object):
    """ OS information model """
    name: str
    accuracy: str
    line: str
    osclass: dict
    cpe: str

    def set_fields(self, ip: str, nmap_resulte: str) -> None:
        """ Sets the values of the fields to their corresonding variable """
        nmap_resulte = nmap_resulte[ip]["osmatch"]
        
        for field in self.__annotations__:
            setattr(self, field, nmap_resulte.get(field, None))


    # 'name': 'Linux 2.6.32',
    # 'accuracy': '100',
    # 'line': '55742',
    # 'osclass': {'type': 'general purpose', 'vendor': 'Linux', 'osfamily': 'Linux', 'osgen': '2.6.X', 'accuracy': '100'},
    # 'cpe': 'cpe:/o:linux:linux_kernel:2.6.32'
