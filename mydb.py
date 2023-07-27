import mysql.connector

dataBase = mysql.connector.Connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Aa412002aa*',
)


cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE zoro")

print("ALL DONE!")