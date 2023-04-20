import f1_2020_telemetry
from f1_2020_telemetry.packets import unpack_udp_packet
import socket
import os


class TelemetryUtils:
    def __init__(self, address, port):
        """Constructor for TelemetryUtils

        Args:
            address (String): address of F1 2020 telemetry server to connect to
            port (int): port of F1 2020 telemetry server to connect to
        """
        self.address = address
        self.port = port
        self.TIMEOUT = 5

    def bind(self):
        """Bind to telemetry server
        """
        self.udpSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udpSocket.bind((self.address, self.port))
        self.udpSocket.settimeout(self.TIMEOUT)

    def getPacket(self):
        """Get latest packet from telemetry server

        Raises:
            TimeoutError: when telemetry server cannot be reached within timout limit

        Returns:
            _type_: udpPacket
        """
        try:
            return unpack_udp_packet(self.udpSocket.recv(2048))
        except socket.timeout:
            raise TimeoutError(f"Host {self} could not be reached.")

    def __str__(self):
        """String method for TelemetryUtils

        Returns:
            String: description of object
        """
        return f"{self.server}/:{self.port}"