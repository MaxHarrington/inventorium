import mysql.connector
from mysql.connector import errorcode

print("Connecting to the database.")

db_name = "inventorium"
tables = dict()

# stores SQL query for the item descriptors
tables['item'] = (
            "CREATE TABLE items("
            "id INT(7) NOT NULL AUTO_INCREMENT,"
            "itemname VARCHAR(20) NOT NULL,"
            "cost INT(8) NOT NULL,"
            "quantity INT(7) NOT NULL,"
            "description VARCHAR(50) NOT NULL,"
            "PRIMARY KEY (id))"
        )

config = {open('database.txt')}

# connects to the MySQL server
connect = mysql.connector.connect(user=open('username.txt').readline(), password='')
cursor = connect.cursor()

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name)
        )
    except mysql.connector.Error as error:
        print("Failed creating database: {}".format(error))

# attempts to USE database on MySQL
try:
    connect.database = db_name
except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("No database found. Attempting to create new database...")
        create_database(cursor)
        connect.database = db_name
    else:
        print(error)
        exit(1)

# creates necessary tables in items, if they don't already exist
for name, iterated in list(tables.items()):
    try:
        print("Creating table {}: ".format(name), end='')
        cursor.execute(iterated)
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(error.msg)
    else:
        print("OK")

cursor.close()
connect.close()