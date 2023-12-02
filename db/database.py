from dotenv import dotenv_values
from pymongo import MongoClient
#тут мы подключаем нашу бд на фруктике и нихуя не понимаем, у меня лично почему то не работает
config = dotenv_values(".env")
database_client  = MongoClient(config["Atlas_URI"])
database = database_client[config["MAGAZ"]]