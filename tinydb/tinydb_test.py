from tinydb import TinyDB, Query, where

db = TinyDB('tinydb_test.json')
query = Query()

db.purge()
db.insert({'name': 'Lukasz', 'age': 40})
db.insert({'name': 'Joanna', 'age': 40})
db.insert({'name': 'Maja', 'age': 13})
db.insert({'name': 'Adam', 'age': 7})

db.update({'age':41},query.name == 'Lukasz')

db.update({'car':'Kia'},query.name == 'Lukasz')


print(db.search(query.age >= 40))
print(db.count(query))
print(db.all())

for doc in db.search(where('age') >= 40):
    print(doc['name'])
    print(doc.doc_id)

print(db.get(where('name') == 'Maja'))