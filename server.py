import socket
from zeroconf import Zeroconf, ServiceInfo

host_name = socket.gethostname()
srv_type = "_hffs._tcp.local."
srv_name = host_name + "." + srv_type

info = ServiceInfo(srv_type,
                   srv_name,
                   28888,
                   properties={"a": "b"},
                   addresses=[socket.inet_aton("127.0.0.1")])

zc = Zeroconf()
zc.register_service(info)

input("Press enter to exit...\n")

zc.close()
