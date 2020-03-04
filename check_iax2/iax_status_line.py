from check_iax2.verbose_class import VerboseClass


class IaxStatusLine(VerboseClass):

    line = None
    header = None
    status = None

    def __init__(self, line, header):
        self.line = line
        self.header = header

    def get_start_column(self, needle):
        if needle == 0:
            return needle

        char = self.line[needle]

        while char is not " ":
            needle = needle - 1
            char = self.line[needle]
        return needle

    def get_end_column(self, needle):
        return self.line.find(" ", needle + 1)

    def parse_column(self, needle):
        start = self.get_start_column(needle)
        end = self.get_end_column(start)
        return self.line[start:end].strip()

    def parse(self):
        self.name = self.parse_column(self.header.name)
        self.host = self.parse_column(self.header.host)
        self.mask = self.parse_column(self.header.mask)
        self.port = self.parse_column(self.header.port)
        self.status = self.parse_column(self.header.status)
        self.description = self.parse_column(self.header.description)

        self.update_status()

    def update_status(self):
        if self.status == "OK":
            self.status = 0
        else:
            self.status = 2
        if self.debug_mode:
            print("Status for {}: {}".format(self.name, self.status))

    def __str__(self):
        buffer = []
        for attr, value in self.__dict__.items():
            buffer.append("{}: {}".format(attr, value))

        return "\n".join(buffer)

