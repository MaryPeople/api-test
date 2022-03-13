from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

SERVICE_ACCOUNT_KEY_JSON = "mary-people-test-firebase-adminsdk-d42xf-05ce444e7e.json"

app = FastAPI()

cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_JSON)
default_app = firebase_admin.initialize_app(cred)
db = firestore.AsyncClient()


async def addData():
  doc_ref = db.collection("users").document("alovelace")
  await doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})


@app.get("/")
async def root():
  # await addData()
  return {"message": "Hello World"}


@app.post("/post")
async def post():
  await addData()
  return "new data added to firestore!"
