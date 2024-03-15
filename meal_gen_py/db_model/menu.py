from connection import Connection
from pathlib import Path
from meal_gen_py.db_model.input_validation import *
from meal_gen_py.db_model.model import *


def initialize(initial_path: Path, db_name: str) -> Connection:
    if initial_path != None:
        dug_directory = dig_directory(initial_path, db_name)
        match dug_directory:
            case None:
                return Connection(db_name)
            case _:
                return Connection(dug_directory)
    else:
        return Connection(db_name)

def dig_directory(directory: Path, term: str) -> Path:
    members = [ i for i in directory.iterdir() ]
    for member in members:
        if member.stem == term:
            return Path(Path.cwd, member)
    for subdirectory in [ i for i in members if i.is_dir() ]:
        return dig_directory(subdirectory, term)

def draw_serving_builder_menu(conn: Connection) -> None:
    (user_input, _) = query_user('Enter the serving name:')
    insert_into_table('serving_name', conn, user_input)
    serving_name_id = select_from_table('serving_name_name', conn, user_input)
    for column in ServingNutrient:
        

def draw_menu(conn: Connection) -> None:
    user_selection = int(match_query_user("""
        Enter a new (s)erving
        (E)nter a new meal
        (G)enerate a new 7-day meal plan
        Enter a (c)ustom query          
        """, 
        ["s", "e", "g", "c"], 
        False))
    match user_selection:
        case "s":
            pass
        case "e":
            pass
        case "g":
            pass
        case "c":
            pass