from fastapi import Depends, HTTPException, status
from gainz.settings import Settings
import pymongo
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Developers should be installed mongoDB for their own to check this backend. 
# (For mongoDB installation guide. https://www.mongodb.com/zh-cn/docs/manual/tutorial/install-mongodb-on-os-x/)
# And as time constrict and convenience for test, I don't set any admin password for the database. 
# To Do. 
# 1. Setup remote testing, staging and production DB
# 2. Add admin name and password

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# DB name and Collection (i.e. Table) are hardcode. Will be updated later. 
db = myclient["gainz"]
collection = db["users"]


def get_db():
    return db

def get_collection():
    return collection
