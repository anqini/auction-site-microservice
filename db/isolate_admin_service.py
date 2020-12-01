
#---------- MongoDB ----------#
from datetime import datetime
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

db_names = client.list_database_names()

def checkDB(db_name):
        if db_name in db_names:
                client.drop_database(db_name)

# delete user_db database if exists
checkDB("user_db")
