from check_iax2.verbose_class import VerboseClass
from check_iax2.header import StatusHeader
from check_iax2.iax_status_line import IaxStatusLine
import sys


class IaxParser(VerboseClass):

    buffer = None
    peer = None
    status = 0
    footer = None
    header = None
    peers = []
    status_code = 0
    status_message = None

    def __init__(self, peer, output):
        self.peer = peer
        self.buffer = output

    def parse(self):
        buffer = str(self.buffer.decode('utf-8').strip()).split("\n")
        self.header = StatusHeader(buffer.pop(0))
        self.header.set_debug_mode(self.debug_mode)
        self.header.parse()
        self.footer = buffer.pop()
        for line in buffer:
            peer = IaxStatusLine(line, self.header)
            peer.set_debug_mode(self.debug_mode)
            peer.parse()
            self.peers.append(peer)

        self.update_status()

    def exit(self):
        if self.status_code == 0:
            sys.exit(0)
        else:
            print(self.status_message)
            sys.exit(self.status_code)

    def update_status(self):
        message = []
        status = 0
        for peer in self.peers:
            if peer.status != 0:
                message.append("Peer {} is offline".format(peer.name))
                status = 2

        if self.debug_mode:
            print("Final status for system: {}".format(status))
        if status == 0:
            self.status_code = 0
            self.status_message = ""
        else:
            self.status_code = 2
            self.status_message = "|".join(message)



    def __str__(self):
        buffer = []
        buffer.append("Peer: {}".format(self.peer))
        buffer.append("Debug mode: {}".format(self.debug_mode))
        buffer.append("Verbosity: {}".format(self.verbosity))
        buffer.append("Status: {}".format(self.status))
        buffer.append("Header: {}".format(self.header))
        buffer.append("Footer: {}".format(self.footer))
        return "\n".join(buffer)