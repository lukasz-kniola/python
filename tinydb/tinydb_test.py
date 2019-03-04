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

babcia = {'dob': {'y': 1943, 'm': 1}, 'age': 76, 'address': 'Bydgoszcz', 'car': 'Fiat'}

db.insert({'name': 'Gizela', 'details': babcia})

print(db.count(query))

for doc in db.search(where('age') >= 40):
    print(doc['name'])
    print(doc.doc_id)

print(db.get(where('name') == 'Maja'))
print(db.search((query.details.dob.y == 1943) | (query.age > 40)))

names = db.table('names')
names.insert_multiple([{'name': 'Lukasz'}, {'name': 'Joanna'}, {'name': 'Maja'}, {'name': 'Adam'}])
