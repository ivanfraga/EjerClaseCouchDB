import couchdb
import numpy as np
couch = couchdb.Server('http://admin:1233tana@127.0.0.1:5984')
#db= couch.create('test')
#db=couch['libros1']

'''doc= {'nombre': 'Iván', 'apellido': 'Fraga'}
doc1= {'nombre': 'Paul', 'apellido': 'Sukerberg'}
doc2= {'nombre': 'Raul', 'apellido': 'Jobs'}
doc3= {'nombre': 'Ratatuille', 'apellido': 'Gates'}
doc4= {'nombre': 'Wilfrido', 'apellido': 'Lopez'}
doc5= {'nombre': 'Marta', 'apellido': 'Cusho'}
db.save(doc1)
db.save(doc2)
db.save(doc3)
db.save(doc4)
db.save(doc5)'''
'''for docid in db.view('_all_docs'):
    id = docid['id']
    doc= db[id]
    print(doc)'''
#db1= couch.create('ejer1')
#db1=couch['ejer1']

'''
nombres = ['Rosita', 'Hugo', 'Paco', 'Luis']
for i in range (4):

    doc = {'nombre': nombres[i]}
    db1.save(doc)'''


db2= couch.create('ejer2')
db2=couch['ejer2']
for i in range (100):
    num = np.random.randint(1,101)
    doc = {'Numero': num}
    db2.save(doc)

