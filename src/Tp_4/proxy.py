import os
import platform

class Ping:
    def execute(self, ip: str):
        if ip.startswith("192."):
            self._ping(ip)
        else:
            print(f"[ERROR] Dirección IP '{ip}' no permitida para este método.")

    def executefree(self, ip: str):
        self._ping(ip)

    def _ping(self, ip: str):
        print(f"[INFO] Realizando ping a {ip}...")
        param = "-n" if platform.system().lower() == "windows" else "-c"
        command = f"ping {param} 10 {ip}"
        os.system(command)

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip: str):
        if ip == "192.168.0.254":
            print("[Proxy] Redireccionando ping a www.google.com usando ejecutefree()")
            self.ping.executefree("www.google.com")
        else:
            print(f"[Proxy] Usando método controlado execute() para IP: {ip}")
            self.ping.execute(ip)

if __name__ == "__main__":
    proxy = PingProxy()

    # Caso válido, IP comienza con 192. (pasa por Ping.execute)
    proxy.execute("192.168.1.10")

    # Caso especial, redirige a www.google.com (pasa por Ping.executefree)
    proxy.execute("192.168.0.254")

    # Caso inválido para Ping.execute (rechazado por Ping, no por proxy)
    proxy.execute("10.0.0.1")