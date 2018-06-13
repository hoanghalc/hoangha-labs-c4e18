from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

new_post = {
    'title': 'Bài ca tuổi trẻ',
    'author': 'Hoàng Hà',
    'content': 'Tuổi trẻ này mình cùng nhau, dắt tay đi từ sáng tới đêm'
}

posts.insert_one(new_post)
