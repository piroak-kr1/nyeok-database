from typing import Any, Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from tables import TableBase

# Setup database connection
# NOTE: postgres trust local connections
engine = create_engine("postgresql://superuser:wrong_password@localhost:5432/database")

# Create tables if not exists
TableBase.metadata.create_all(engine)


SessionLocal = sessionmaker(bind=engine)


def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
