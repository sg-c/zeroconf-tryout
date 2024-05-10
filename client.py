import socket
from zeroconf import ServiceStateChange, Zeroconf, ServiceBrowser, ServiceListener


class HffsServiceListner(ServiceListener):
    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        info = zc.get_service_info(type_, name)
        print(f"Service {name} added, service info: {info}")


srv_type = "_hffs._tcp.local."

zc = Zeroconf()
listener = HffsServiceListner()
browser = ServiceBrowser(zc, srv_type, listener=listener)

input("Enter to exit...\n\n")

zc.close()
