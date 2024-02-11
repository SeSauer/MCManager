from pathlib import Path
from MCManager.backend.ServerModel.Server import Server
from MCManager.backend.ServerModel.ServerStatus import ServerStatus
from MCManager.backend.ServerModel.ServerExecutables.ServerExecutableInterface import ServerExecutableInterface
from MCManager.backend.ServerModel.ServerExecutables.ExecutableFactory import get_executable


class ServerManager:

    def __init__(self, name: str, server: Server, exec_path: Path, args: str = ""):
        self.server: Server = server
        self.args: str = args
        self.name: str = name
        self.executable: ServerExecutableInterface = get_executable(exec_path)

    def get_status(self) -> ServerStatus:
        raise NotImplementedError

    def deploy_command(self, command: str):
        raise NotImplementedError