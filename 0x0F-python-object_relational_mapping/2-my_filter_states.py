#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
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
    query = "SELECT *FROM states WHERE name = '{:s}' \
            ORDER by states.id ASC".format(sys.argv[4])
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for result in myresult:
        if result[1] == sys.argv[4]:
            print(result)
