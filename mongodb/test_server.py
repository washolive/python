"""
Verifica instalação server do MongoDB
"""

from pymongo import MongoClient
from pprint import pprint

# Cria um client
client = MongoClient('localhost', 27017)

# Conecta-se ao database "admin"
db = client.admin

# Verifica o status do server
status = db.command("serverStatus")
pprint(status)
