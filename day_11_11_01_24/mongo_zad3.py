from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi

# python -m pip install "pymongo[srv]"==3.12
# pip install pymongo[srv]==3.12
uri = ""

client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)
# Pinged your deployment. You successfully connected to MongoDB!
#
# Process finished with exit code 0
