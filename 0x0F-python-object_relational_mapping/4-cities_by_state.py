#!/usr/bin/python3
"""
cript that lists all cities from the database
hbtn_0e_4_usa
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
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY id ASC
    """
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for result in myresult:
        print(result)
