#!/usr/bin/python3
"""
lists all State objects from the database
hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    natijat = session.query(State).filter_by(id=2).first()
    natijat.name = "New Mexico"
    session.commit()
