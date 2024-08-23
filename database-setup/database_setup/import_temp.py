if __name__ == "__main__":
    print("Database Core")

    from database_core import db

    print(db.SessionLocal)

    from database_core import tables

    print(tables.Place.metadata.tables)

    from database_core import crud_temp

    crud_temp.main()
