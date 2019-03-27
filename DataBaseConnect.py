import pymongo
from pprint import pprint
import datetime

##conect to mongo__db
client =  pymongo.MongoClient("mongodb+srv://catifi:catifi2019@cluster0-xx7l9.gcp.mongodb.net/test?retryWrites=true")
#acsess to dv
db = client.testDB
#accses to  collection in db
collection = db.Demo

#create db
"""""
post = {"author": "Mike",
"text": "My first blog post!",
"tags": ["mongodb", "python", "pymongo"],
"date": datetime.datetime.utcnow()}
posts = db.posts
post_id = posts.insert_one(post).inserted_id

db.collection_names(include_system_collections=False)
print(posts.find_one())
"""

print(collection.find_one())





