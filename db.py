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


    @staticmethod
    def create_table(table_name: str) -> str:
        if not Database.has_table(table_name):
            open(f"{table_name}.txt", "w")
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
        open(f"{table_name}.txt", "w").write(columns)

    @staticmethod
    def write_values(table_name: str, **kwargs):
        if not Database.has_table(table_name):
            return "Table does not exist"
        table = Database.get_table(table_name)
        table_columns = Database.get_columns(table_name)
        data = ""
        if Database.has_autoincrement(table_name, Database.get_columns(table_name)[0]):
            pass
        for val in kwargs:
            data += f"{val}, "
        data = data[:-2]
        if not len(kwargs) == len(table_columns) and not len(kwargs) == len(table_columns) - 1:
            return "the amount of columns does not match the amount of data to be written"
        open(table, "a").write(f"\n{data}")
        

    @staticmethod
    def create_database(db_name: str):
        os.mkdir(db_name)

    # Wont actually know if it worked, unless we actually created two or more database
    @staticmethod
    def use_database(db_name: str):
        os.chdir(db_name)

    @staticmethod
    def get_columns(table_name: str) -> list[str]:
        string_column = open(Database.get_table(table_name), "r").readline().rstrip()
        return string_column.split(", ")

    @staticmethod
    def get_table(table_name: str):
        return f"{table_name}.txt" if f"{table_name}.txt" in os.listdir() else "table does not exist"

    @staticmethod
    def has_table(table_name: str):
        return True if f"{table_name}.txt" in os.listdir() else False
    
    @staticmethod
    def has_autoincrement(table_name: str, column_name: str):
        if AUTOINCREMENT in column_name:
            with open(table_name, "rb") as read_file:
                read_file.seek(0, 2)
                position = read_file.tell()
                while position > 0:
                    read_file.seek(position - 1)
                    if read_file.read(1) == b"\n":
                        break
                    position -= 1
                column = read_file.readline().decode()
            get_id = ""
            for char in column:
                if char == ",":
                    break
                get_id += char
            return int(get_id)

if __name__ == "__main__":
    Database.use_database("this_db")
    print(Database.has_autoincrement("my_table.txt", "tite_id autoincrement"))
    #print(Database.create_columns("testing", 
    #               tite="testing_id autoincrement pk", 
    #               hotdog="test_name text",
    #               test_age="test_age int"))