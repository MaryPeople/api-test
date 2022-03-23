from fastapi import HTTPException
from firebase import collection_ref, doc_ref
from datetime import datetime
from pydantic import BaseModel


class User(BaseModel):
  uid: str = None
  name: str = ""
  age: int = None
  last_login: datetime = datetime.now()
  admin: bool = False


async def create_user(user: User):
  try:
    await doc_ref(user.uid).set({**user.dict()})
  except:
    raise HTTPException(status_code=404, detail="UserNotFound")


async def get_users():
  docs = collection_ref("Users").stream()
  userlist = []
  async for doc in docs:
    userlist.append(doc.to_dict())
  return userlist


async def update_username(uid: str, name: str):
  try:
    await doc_ref(uid).update({"name": name})
  except:
    raise HTTPException(status_code=404, detail="UserNotFound")


async def delete_user(uid: str):
  try:
    await doc_ref(uid).delete()
  except:
    raise HTTPException(status_code=404, detail="UserNotFound")
