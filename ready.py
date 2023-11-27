import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.document("人選之人/BKFrrMmNwVM04Z7JgYSS")
doc = doc_ref.get()
result = doc.to_dict()
print(result)
print(result["name"])
print(result["lab"])