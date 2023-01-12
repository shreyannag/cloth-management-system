from mysql.connector import *
try:
    # connector
    db = connect(
        host="127.0.0.1",
        user="root",
        password=""
    )
    conn = db.cursor()
    # generating the main system database
    print("Creating the database.......")
    conn.execute("create database cms")
    db.commit()
except:
    print("Database already exists")
    conn.close()
    db.close()