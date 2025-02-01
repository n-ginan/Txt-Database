import utils
import os

DATABASE_DIRECTORY = "database"
DATA_TYPE_INT = "int"
DATA_TYPE_TEXT = "text"
DATA_TYPE_FLOAT = "float"
PRIMARY_KEY = "pk"
FOREIGN_KEY = "fk"
AUTOINCREMENT = "autoincrement"

class Database:

    __tables = []
    __database = ""

    @staticmethod
    def create_table(table_name: str) -> str:
        if not DATABASE_DIRECTORY in os.listdir():
            os.mkdir(DATABASE_DIRECTORY)
        if not Database.has_table(table_name):
            os.chdir("database")
            open(f"{table_name}.txt", "w")
            Database.__tables.append(f"{table_name}.txt")
            return "table successfully created"
        return "table already exists"

    @staticmethod
    def create_columns(table_name: str, **kwargs):
        if not Database.has_table(table_name):
            return "table does not exist in the database"
        columns = ""
        for column in kwargs.values():
            columns += f"{column}, "
        columns = columns[:-2]
        if DATABASE_DIRECTORY in os.listdir():
            os.chdir("database")
            open(f"{table_name}.txt", "w").write(columns)

    def write_values(table_name: str, **kwargs):
        pass

    @staticmethod
    def create_database(db_name: str):
        os.mkdir(db_name)
        Database.__database = db_name

    # Wont actually know if it worked, unless we actually created two or more database
    @staticmethod
    def use_database(db_name: str):
        os.chdir(db_name)
        return Database.__database   

    @staticmethod
    def get_table(table_name: str):
        return f"{table_name}.txt" if f"{table_name}.txt" in os.listdir() else "table does not exist"

    @staticmethod
    def has_table(table_name: str):
        return True if f"{table_name}.txt" in Database.__tables else False

if __name__ == "__main__":
    Database.create_database("this_db")
    #print(Database.create_columns("testing", 
    #               tite="testing_id autoincrement pk", 
    #               hotdog="test_name text",
    #               test_age="test_age int"))