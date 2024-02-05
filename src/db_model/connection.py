import sqlite3, os
from src.db_model.input_validation import *
from model import *

class ConnectionError(Exception):
    pass

class Connection:
    def __init__(self, path):
        self.__path = path

    def establish_connection(self):
        conn = sqlite3.connect(self.path())
        conn.autocommit = False
        if conn != None:
            self.connection = conn
        else:
            raise ConnectionError(f'Could not establish connection with {self.path()}')

    def checked_establish_connection(self):
        if os.path.exists(self.__path):
            self.establish_connection()
        else:
            confirmation = match_query_user(f'No database was found at {self.path()}. Would you like to create one? (y, N) ', ['y', 'n', None], False)
            match confirmation:
                case None:
                    print(f'Did not create database at {self.path()}.')
                case 'y' | 'Y':
                     self.establish_connection()
                case _:
                    print(f'Did not create database at {self.path()}.')

    def generate_cursor(self):
        cursor = self.connection.cursor()
        # cursor.row_factory = namedtuple_factory
        cursor.row_factory = dict_factory
        return cursor
    
    def commit(self):
        self.connection.commit()

    def path(self):
        return self.__path

def flash_db_build(path, conn):
    cur = conn.generate_cursor()
    with open(path, 'r') as build:
        sql_script = build.read()
    cur.executescript(sql_script)
    conn.commit()