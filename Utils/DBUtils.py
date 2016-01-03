import pymongo
from pymongo.errors import ServerSelectionTimeoutError


def get_mongodb(database_host, database_port, database_name, database_username, database_password):
    try:
        client = pymongo.MongoClient(
            host=database_host,
            port=database_port
        )
        db = client.get_database(database_name)
        db.authenticate(database_username, database_password)
    except ServerSelectionTimeoutError as err:
        print(ServerSelectionTimeoutError, err, 'timed out')
        return

    return db


