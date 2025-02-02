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
        table_columns = Database.get_columns(table)
        data = ""
        if Database._has_auto_increment(Database.get_columns(table)[0]):
            if len(open(table, "r").readlines()) >= 0:
                data += f"{Database.__autoincrement(table) + 1}, "
            else:
                data += "0, "
        for val in kwargs.values():
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
        string_column = open(table_name, "r").readline().rstrip()
        return string_column.split(", ")

    @staticmethod
    def get_table(table_name: str):
        return f"{table_name}.txt" if f"{table_name}.txt" in os.listdir() else "table does not exist"

    @staticmethod
    def has_table(table_name: str):
        return True if f"{table_name}.txt" in os.listdir() else False
    
    @staticmethod
    def _has_auto_increment(column_name: str):
        return True if AUTOINCREMENT in column_name else False

    @staticmethod
    def __autoincrement(table_name: str):
        with open(table_name, "rb") as read_file:
            read_file.seek(0, os.SEEK_END)
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
    print(Database.write_values("my_table", name="emperor", age="12"))
    #print(Database.create_columns("testing", 
    #               tite="testing_id autoincrement pk", 
    #               hotdog="test_name text",
    #               test_age="test_age int"))