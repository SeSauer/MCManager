from pathlib import Path
from typing import Protocol


class ServerExecutableInterface(Protocol):

    def execute(self):
        raise NotImplementedError

    def get_path(self):
        raise NotImplementedError