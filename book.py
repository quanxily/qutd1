import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection("圖書精選")
docs = collection_ref.order_by("date",direction=firestore.Query.DESCENDING).get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))