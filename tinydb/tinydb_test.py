from tinydb import TinyDB, Query, where

db = TinyDB('tinydb_test.json')
query = Query()

family = db.table('family')

family.purge()
family.insert({'name': 'Lukasz', 'age': 40})
family.insert({'name': 'Joanna', 'age': 40})
family.insert({'name': 'Maja', 'age': 13})
family.insert({'name': 'Adam', 'age': 7})

family.update({'age':41},query.name == 'Lukasz')

family.update({'car':'Kia'},query.name == 'Lukasz')

babcia = {'dob': {'y': 1943, 'm': 1}, 'age': 76, 'address': 'Bydgoszcz', 'car': 'Fiat'}

family.insert({'name': 'Gizela', 'details': babcia})

print(family.count(query))

for doc in family.search(where('age') >= 40):
    print(doc['name'])
    print(doc.doc_id)

print(family.get(where('name') == 'Maja'))
print(family.search((query.details.dob.y == 1943) | (query.age > 40)))

names = db.table('names')
names.insert_multiple([{'name': 'Lukasz'}, {'name': 'Joanna'}, {'name': 'Maja'}, {'name': 'Adam'}])
