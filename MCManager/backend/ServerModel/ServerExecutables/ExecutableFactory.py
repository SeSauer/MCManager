from pathlib import Path
from MCManager.backend.ServerModel.ServerExecutables.JarExecutable import JarExecutable
from MCManager.backend.ServerModel.ServerExecutables.ServerExecutableInterface import ServerExecutableInterface


def get_executable(path: Path) -> ServerExecutableInterface:
    if path.suffix == '.jar':
        return JarExecutable(path)
    else:
        raise Exception('Cannot build Executable: Invalid file ending')