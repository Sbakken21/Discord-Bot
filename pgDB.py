import psycopg2
import configparser

#load the configuration
config = configparser.ConfigParser()
config.read('jojobot.cfg')

"""
    CONNECTION TO POSTGRESQL DATABASE
"""

# PostgreSQL DB connection
conn = psycopg2.connect(
    database = config.get("database", "database"),
    user = config.get("database", "user"),
    password = config.get("database", "password"),
    host = config.get("database", "host"),
    port = config.get("database", "port")
)

print("Connecting to database %s" % (conn))

cur = conn.cursor()
print("Connected to DB")

# Create a new table with a single column called "name"
# cur.execute("CREATE TABLE dodge (name text);")

# Create a new table for reminders
# cur.execute("CREATE TABLE reminder (user text, message text, time);")

"""
    COMMANDS FOR DODGE LIST DB
"""

def add_name(summoner):
    query = "INSERT INTO dodge (name) VALUES (%s);"
    data = (summoner,)
    cur.execute(query, data)
    # cur.execute("INSERT INTO test (name) VALUE ('testing')")
    conn.commit()

def view_list():
    cur.execute("SELECT name from dodge")
    rows = cur.fetchall()

    return rows

def remove_name(del_name):
    cur.execute("SELECT name from dodge")
    sql = "DELETE FROM dodge WHERE LOWER(name) = %s;"
    lower = del_name.lower()
    data = (lower,)
    cur.execute(sql, data)
    conn.commit()

