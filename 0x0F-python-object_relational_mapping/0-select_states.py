#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":

    mydb = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
            )

    mycursor = mydb.cursor()
    query = "SELECT *FROM states"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for result in myresult:
        print(result)
