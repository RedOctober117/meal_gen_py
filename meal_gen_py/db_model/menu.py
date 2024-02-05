from connection import Connection
from pathlib import Path


def initialize(initial_path: Path, db_name: str):
    if initial_path != None:
        dug_directory = dig_directory(initial_path, db_name)
        match dug_directory:
            case None:
                return Connection(db_name)
            case _:
                return Connection(dug_directory)
    else:
        return Connection(db_name)

def dig_directory(directory: Path, term: str):
    members = [ i for i in directory.iterdir() ]
    for member in members:
        if member.stem == term:
            return Path(Path.cwd, member)
    for subdirectory in [ i for i in members if i.is_dir() ]:
        return dig_directory(subdirectory, term)

