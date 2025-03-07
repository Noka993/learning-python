import sqlite3
from database import *

create_table_sql_statement = 'CREATE TABLE IF NOT EXISTS books(title TEXT, author TEXT)'
insert_into_table_sql_statement = "INSERT INTO books VALUES ('If Tomorrow Comes', 'Sidney Sheldon'), ('The Lincoln Lawyer', 'Michael Connelly')"
select_from_table_sql_statement = 'SELECT * FROM books'

def main():
    with Database('memory') as db:
        db.cursor.execute(create_table_sql_statement)
        db.connection.commit()
        
        db.cursor.execute(insert_into_table_sql_statement)
        db.connection.commit()
        
        db.cursor.execute(select_from_table_sql_statement)

        print(db.cursor.fetchall())

if __name__ == '__main__':
    main()