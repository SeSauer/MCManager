from pathlib import Path

from MCManager.backend.ServerModel.Server import Server
from MCManager.backend.ServerModel.ServerManager import ServerManager
from MCManager.backend.save_load import save_load
from MCManager.backend.ServerModel.ServerCollection import ServerCollection


class Manager:

    def __init__(self, load: bool):
        self.server_collection = ServerCollection()
        if load:
            for server in save_load.load():
                self.server_collection.register(server)

    def get_server(self, name: str) -> ServerManager:
        return self.server_collection.get_server(name)

manager: Manager

def init(instance_path: str):
    global manager
    save_load.save_path = Path(instance_path) / "saves.json"
    manager = Manager(True)