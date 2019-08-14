import mysql.connector as mysqlConnector
import json


class DbConnection:
    def __init__(self):
        self.mydb = mysqlConnector.connect(
            host="localhost",
            user="root",
            password="rootmysql",
            database="user_directory"
        )

    def getcursor(self):
        return self.mydb.cursor()

    def getconnection(self):
        return self.mydb

    def getRules(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM rules")
        myresult = cursor.fetchall()
        for rule in myresult:
            print "rule id: %s, customer_id: %s " %(rule[0], rule[2])


if __name__ == '__main__':
    print("Invoking dbmanager main function")
    xx = DbConnection()
    xx.getRules()



