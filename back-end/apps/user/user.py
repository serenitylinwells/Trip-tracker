import hashlib
from uuid import uuid1
from fastapi import APIRouter
from datetime import datetime
from ..orm.models import *

userApi = APIRouter()

def hash_md5(string: str) -> str:
    md5 = hashlib.md5()
    md5.update(string.encode("utf-8"))
    return md5.hexdigest()

@userApi.post("/login")  # Login interface
async def login(user: UserLogin):
    # Login: convert the password to md5 and compare it with the corresponding password MD5 of the username
    duser = await Users.filter(username=user.username).first()
    if duser and duser.password == hash_md5(user.password):
        # Generate token: use the unique user UUID + current date, convert it to md5
        return {"status": "SUCCEED", "token": hash_md5((duser.uuid + datetime.now().strftime("%Y%m%d")))}
    else:
        return {"status": "ERROR", "token": None}

@userApi.post("/register")  # Registration interface
async def register(user: UserRegister):
    # Convert the user password to md5
    try:
        newuser = await Users.create(uuid=uuid1(), mail=user.mail, username=user.username,
                                     password=hash_md5(user.password))
    except:
        return {"status": "FAIL", "username": None}
    return {"status": "SUCCEED", "username": newuser.username}
