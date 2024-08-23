# Setup database connection and expose

from typing import Any, Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session


# NOTE: postgres trust local connections
# TODO: make as environment variable (also in alembic.ini)
engine = create_engine("postgresql://superuser:wrong_password@localhost:5432/database")

# NOTE: Do not create table - Alembic will manage schema
# Create tables if not exists
# TableBase.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)


def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
