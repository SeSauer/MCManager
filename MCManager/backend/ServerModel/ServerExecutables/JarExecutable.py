from pathlib import Path
from subprocess import Popen, PIPE
from MCManager.backend.ServerModel.ServerExecutables.ServerExecutableInterface import ServerExecutableInterface

class JarExecutable(ServerExecutableInterface):

    def __init__(self, path: Path):
        self.path = path

    def execute(self) -> Popen:
        raise NotImplementedError

    def get_path(self) -> Path:
        return self.path