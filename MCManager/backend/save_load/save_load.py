import json
from pathlib import Path

from MCManager.backend.ServerModel.ServerManager import ServerManager
from MCManager.backend.ServerModel.Server import Server

save_path: Path

def save(server_manager: ServerManager):
    json_to_save = {
        'folder': server_manager.server.folder.__str__(),
        'name': server_manager.name,
        'exec_path': server_manager.executable.get_path().__str__(),
        'args': server_manager.args
    }
    with open(save_path, 'a') as f:
        f.write(json.dumps(json_to_save) + "\n")

def load() -> list[ServerManager]:
    output: list[ServerManager] = []
    if save_path.stat().st_size == 0:
        return output
    with open(save_path, 'r') as f:
        savefile: json = json.load(f)
    for server_instance in savefile:
        server: Server = Server(Path(server_instance["folder"]))
        manager = ServerManager(server=server,
                                exec_path=Path(server_instance["exec_path"]),
                                name=server_instance["name"],
                                args=server_instance["args"])
        output.append(manager)
    return output
