# Database -> Collection -> Document

from pymongo import MongoClient

mongo_uri = "mongodb://hoangha-c4e-ss1:matkhau@ds147390.mlab.com:47390/c4e18-labs-ss1"

#1. Connect to Database
client = MongoClient(mongo_uri)


#2. Get Database
db = client.get_default_database()

#3. Creat Collection
games =  db['games']
# classmate = db['classmates']

#4. Creat Document
new_game = {
    "title": 'PUBG',
    "description": "Survival"
}

# new_friend = {
#     "title": "Duy",
#     "description": "oc cho"
# }

#5. Insert Document into Collection
# games.insert_one(new_game)
# classmate.insert_one(new_friend)


all_game = games.find()
for game in all_game:
    print(game)