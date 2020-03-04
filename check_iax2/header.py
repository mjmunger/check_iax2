from check_iax2.verbose_class import VerboseClass


class StatusHeader(VerboseClass):

    raw_header = None
    name = None
    host = None
    mask = None
    port = None
    status = None
    Description = None

    def __init__(self, header):
        self.raw_header = header

    def parse(self):
        self.name = self.raw_header.find("Name")
        self.host = self.raw_header.find("Host")
        self.mask = self.raw_header.find("Mask")
        self.port = self.raw_header.find("Port")
        self.status = self.raw_header.find("Status")
        self.description = self.raw_header.find("Description")

    def __str__(self):
        buffer = []
        for attr, value in self.__dict__.items():
            buffer.append("{}: {}".format(attr, value))

        return "\n".join(buffer)