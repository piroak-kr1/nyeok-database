from db import SessionLocal
from tables import Place


def insert_one():
    with SessionLocal() as session, session.begin():
        place1 = Place(contentid=2, title="test", firstimage2=".jpg")
        session.add(place1)


def delete_all():
    with SessionLocal() as session:
        session.query(Place).delete()
        session.commit()


def query_all():
    with SessionLocal() as session:
        return session.query(Place).all()


def main():
    delete_all()
    insert_one()
    print(query_all())
