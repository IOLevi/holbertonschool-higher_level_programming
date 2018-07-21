#!/usr/bin/python3
#prints first State obj from the database hbtn_0e_6_usa

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first() # HERE: no SQL query, only objects!
    if first == None:#fix this later
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
    session.close()