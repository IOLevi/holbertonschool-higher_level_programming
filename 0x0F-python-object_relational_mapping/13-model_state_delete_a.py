#!/usr/bin/python3
# deletes all State objects containing the letter a from the database

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    # HERE: no SQL query, only objects!
    query = session.query(State).filter(State.name.contains('a'))
    query.delete(synchronize_session=False)
    session.commit()
    session.close()
