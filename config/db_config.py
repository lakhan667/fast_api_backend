import mysql.connector

def get_db_connection():
    try:
        myconn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydemodb"
        )
        return myconn
    except Exception as e:
        print(e)
        return None