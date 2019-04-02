import pymongo
from CsvReader import l
client = pymongo.MongoClient("mongodb+srv://YardenNew:yarden@cluster0-xx7l9.gcp.mongodb.net/test?retryWrites=true")
db = client.test
print(db)
#Working example of insert code to mongodb from pycharm see as refernce
# dictJS = {'re: ': 'Testing Insert'}
# client.test.check.insert_one({
#     "_id": 2,
#     "name": "pizza",
#     "calories": 234,
#     "fats": {
#         "saturated": 1.5,
#         "trans": 0.3
#     },
#     "protein": 11
# })

insert_dict_to_DB = {'MAC_ADRESS','DNS_ARRAY'}

for Index_array in l:
 client.test.check.insert_one({
     "Id": l.id,"mac":l.mac,
     "Dns" : l.dns})