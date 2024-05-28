from pymongo import MongoClient

# Base de Datos Local
# db_client = MongoClient().local

# Base de Datos Remota
db_client = MongoClient("mongodb+srv://jlguerrerotoria:dncrlM8itUAT0Bqx@cluster0.lvy5jil.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test
