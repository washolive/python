"""
Cria um database no mongodb.

MongoDB não tem um comando específico para criar o database.
O comando "use" é utlizado para selecionar ou mudar de database. O MongoDB
verifica se existe: se existir, conecta-se nele; se não existir, cria ele.

Exemplo no MongoSh:
> use dbwash
< 'switched to db dbwash'
> db
< dbwash
"""

from  pymongo import MongoClient

# Cria um client
client = MongoClient('localhost', 27017)

# Seleciona um database que ainda não existe
db = client['exemplo']
print("Database 'exemplo' criado!")

# Cria uma collection de teste neste database
db.create_collection('teste')

# Verifica se o database foi criado
print("Lista dos databases existentes:")
print(client.list_database_names())
