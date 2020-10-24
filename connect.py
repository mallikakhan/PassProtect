import mysql.connector as con

def connector():
    mydb = con.connect(
    	host = 'localhost',
    	user = 'root',
    	passwd = 'info9crypt1',
        database = 'PassProtect'
    )

    return mydb

# print(connector())
