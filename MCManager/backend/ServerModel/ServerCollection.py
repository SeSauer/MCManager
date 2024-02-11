from MCManager.backend.ServerModel.ServerManager import ServerManager


class ServerCollection():

    def __init__(self):
        self.servers: list[ServerManager] = []

    def register(self, server):
        if server in self.servers:
            raise Exception("Server already registered")
        self.servers.append(server)

    def get_server(self, name: str) -> ServerManager:
        return next((x for x in self.servers if x.name == name), None)
