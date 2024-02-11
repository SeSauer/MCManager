from typing import Protocol


class ServerCreatorInterface(Protocol):

    REQUESTED_IDENTIFIER = "Unknown"

    def add_server(self, name: str, identifier: str):
        raise NotImplementedError