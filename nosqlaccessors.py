from pymongo import MongoClient
from datetime import datetime

client = MongoClient()
db = client.ils #ils is dbname

def queryMongo(query, *projection):
    if len(projection) > 0:
        ans = db.books.find(query, projection[0]) #books is collection
    else:
        ans = db.books.find(query)
    return list(ans)

def distinctMongo(query):
    ans = db.books.distinct(query)
    return list(ans)
##queryproj = {'_id': 1, 'title': 1, 'isbn': 1, 'pageCount': 1, 'authors': 1, 'categories': 1}
##testans = queryMongo({"_id": 1}, queryproj)
##print(testans)
##returns [{'_id': 1, 'title': 'Unlocking Android', 'isbn': '1933988673'}, {'_id': 2, 'title': 'Android in Action, Second Edition', 'isbn': '1935182722'}]

#testans3 = queryMongo({"title":{"$regex": "droid"}}, {"_id":1})
#print(testans3)

#testans5 = queryMongo({"$and": [{"title":{"$regex": "lock"}},{"categories": {"$eq": "Open Source"}},{"categories": {"$eq": "Mobile"}}, {"authors": {"$elemMatch":{"$regex": "Sen"}}}]},{"_id":1})
#print(testans5)

#value = {}
#value["$regex"] = "droid"
#testans31 = queryMongo({"title":value}, {"_id":1})
#print(testans31)
##returns [{'_id': 1}, {'_id': 2}, {'_id': 54}, {'_id': 165}, {'_id': 514}, {'_id': 580}]


#from_date = datetime(2010, 1, 1)
#to_date = datetime(2011, 1, 1)
#testans4 = queryMongo({"publishedDate":{"$gte": from_date, "$lt": to_date}}, {"_id":1})
#print(testans4)

#print(distinctMongo("categories"))
##returns ['', '.NET', 'Algorithmic Art', 'Business', 'Client Server',
##'Client-Server', 'Computer Graph', 'Computer Graphics', 'In Action',
##'Internet', 'Java', 'Microsoft', 'Microsoft .NET', 'Microsoft/.NET',
##'Miscella', 'Miscellaneous', 'Mobile', 'Mobile Technology', 'Networking',
##'Next Generation Databases', 'Object-Oriented Programming',
##'Object-Technology Programming', 'Open Source', 'P', 'PHP', 'Perl',
##'PowerBuilder', 'Programming', 'Python', 'S', 'SOA', 'Software Development',
##'Software Engineering', 'Theory', 'Web Development', 'XML', 'internet', 'java']
