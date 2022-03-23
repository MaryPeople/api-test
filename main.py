from fastapi import FastAPI
import crud
from crud import User

app = FastAPI()


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.post('/users')
async def create_user(user: User):
  await crud.create_user(user=user)
  return {
      "message": "user created!",
      "body": user
  }


@app.get('/users')
async def get_users():
  userlist = await crud.get_users()
  return {
      "message": "read all users!",
      "body": userlist
  }


@app.post('/users/{uid}')
async def update_username(uid: str, name: str):
  await crud.update_username(uid=uid, name=name)
  return {
      "message": "updated user name!",
  }


@app.delete('/users/{uid}')
async def delete_user(uid: str):
  await crud.delete_user(uid=uid)
  return {
      "message": "deleted user!"
  }
