from pathlib import Path

class Server:
    def __init__(self, folder: Path):
        self.folder: Path = folder

    def edit_server_property(self, property: str, value: str):
        raise NotImplementedError

    def edit_whitelist(self, player_name: str, status: bool):
        raise NotImplementedError