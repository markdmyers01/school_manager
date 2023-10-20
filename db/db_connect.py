import sys
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = create_engine('sqlite:///course_data.db', echo=True)
except SQLAlchemyError as err:
    print(f'Error connecting to database.  Error: {err}', file=sys.stderr)
    sys.exit()
