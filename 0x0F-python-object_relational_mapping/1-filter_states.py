#!/usr/bin/python3
"""
script that lists all states with a name starting with N
upper N) from the database hbtn_0e_0_usa
"""
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
    query = "SELECT *FROM states WHERE name LIKE 'N%'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for result in myresult:
        if result[1][0] == 'N':
            print(result)
