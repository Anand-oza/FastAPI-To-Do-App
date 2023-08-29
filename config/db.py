from pymongo import MongoClient

MONGO_URI = "mongodb+srv://<username>:<password>@<clusterName>.mongodb.net"

conn = MongoClient(MONGO_URI)