import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

docs = [
{
  "name": "賴清德",
  "mail": "委員",
  "lab": 1959
},

{
  "name": "林宜蓁",
  "mail": "委員",
  "date":1966
},

{
  "name": "蔡英文",
  "roul": "總統",
  "date": 1956
}

{
  "name": "黃建偉",
  "roul": "公正黨文宣部主任",
  "date": 1977
}

{
  "name": "楊荃喜",
  "roul": "靜宜大學資訊管理",
  "date": 2004
}

]

collection_ref = db.collection("人選之人")
for doc in docs:
  collection_ref.add(doc)
