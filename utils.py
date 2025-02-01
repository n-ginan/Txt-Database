import db
import os

def has_explicit_pk_id(column_name: str) -> bool:
    column_properties = column_name.split(" ")
    return (True if db.AUTOINCREMENT in column_properties 
            or db.PRIMARY_KEY in column_properties else False)

def has_fk_table(table_name = str, referenced_table_name = str | list[str]):
    if db.DATABASE_DIRECTORY in os.listdir():
        os.chdir(db.DATABASE_DIRECTORY)
        if f"{referenced_table_name}.txt" in os.listdir() and not table_name == referenced_table_name:
            return True
    return False

if __name__ == "__main__":
    print(has_fk_table("testing", "behave"))