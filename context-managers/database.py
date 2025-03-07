import sqlite3
from contextlib import contextmanager

class Database:
    # OOP type context manager
    def __init__(self, path: str):
        self.path = path
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'an error occurred: {exc_val}')
            
        self.connection.close()

@contextmanager
def database(path: str):
    # Generator based context manager
    connection = sqlite3.connect(path)
    try:
        cursor = connection.cursor()
        yield {'connection': connection, 'cursor': cursor}
    except Exception as e:
        print(f'an error occurred: {e}') 
    finally:
        connection.close()