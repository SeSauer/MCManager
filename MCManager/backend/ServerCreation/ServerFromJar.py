from pathlib import Path
from MCManager.backend.ServerModel.Server import Server
from MCManager.backend.ServerModel.ServerCollection import ServerCollection
from MCManager.backend.ServerModel.ServerManager import ServerManager
from MCManager.backend.ServerCreation.ServerCreatorInterface import ServerCreatorInterface
from MCManager.backend.save_load import save_load


class ServerFromJar(ServerCreatorInterface):

    REQUESTED_IDENTIFIER = "Jar file representing the Minecraft Server"

    def __init__(self, server_collection: ServerCollection):
        self.server_collection = server_collection


    def add_server(self, name: str, identifier: str):
        exec_path: Path = Path(identifier)
        if not exec_path.suffix == ".jar":
            raise Exception("Not a Jar file")
        server = Server(exec_path.parent)
        server_manager = ServerManager(name=name,
                                       server=server,
                                       exec_path=exec_path)
        self.server_collection.register(server_manager)
        save_load.save(server_manager)

