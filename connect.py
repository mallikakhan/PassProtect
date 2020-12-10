import mysql.connector


def connector():
    mydb = mysql.connector.connect(host="localhost", user="root", password="mumu2000", database="passprotect")
    return(mydb)

# print(connector())
