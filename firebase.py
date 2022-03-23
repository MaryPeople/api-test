import firebase_admin
from firebase_admin import credentials, firestore

SERVICE_ACCOUNT_KEY_JSON = "mary-people-test-firebase-adminsdk-d42xf-05ce444e7e.json"

cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_JSON)
default_app = firebase_admin.initialize_app(cred)
db = firestore.AsyncClient()


def collection_ref(collection_name: str):
  return db.collection(collection_name)


def doc_ref(doc_name: str):
  return db.collection("Users").document(doc_name)
