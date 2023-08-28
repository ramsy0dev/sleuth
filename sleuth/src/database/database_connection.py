from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import postgresql

class DatabaseConnection:
    """ Creates a connection a database wither it's SQLite or Postgresql """
    def __init__(self, database_url: str) -> None:
        try:
            self.engine = create_engine(
                database_url,
                # dialect=postgresql.dialect()
            )
            self.Session = sessionmaker(bind=self.engine)
        except exc.SQLAlchemyError as error:
            raise error
