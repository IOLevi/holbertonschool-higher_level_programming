#!/usr/bin/python3
#adds the state object "Louisiana" to the database

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    lou = State(name="Louisiana")
    session.add(lou)
    session.commit()
    #forgot to print id of the newly created state
    print(lou.id)
    session.close()