from pydantic import BaseModel
from tortoise import fields
from tortoise.models import Model


class RouteInfo(BaseModel):
    startPointName: str  # Start point name, string type
    startPointSign: str  # Start point sign, string type
    endPointName: str  # End point name, string type
    endPointSign: str  # End point sign, string type


class Site(BaseModel):
    keywords: str  # Keywords, string type


class UserLogin(BaseModel):
    username: str  # Username, string type
    password: str  # Password, string type


class UserRegister(BaseModel):
    username: str  # Username, string type
    password: str  # Password, string type
    mail: str  # Email, string type


class UserReset(BaseModel):
    username: str  # Username, string type
    password: str  # Password, string type
    newpassword: str  # New password, string type


class Users(Model):
    # id field, integer type, used as primary key
    id = fields.IntField(pk=True)
    # uuid field, character type, maximum length of 36, unique constraint
    uuid = fields.CharField(max_length=36, description='User UUID', unique=True)
    # email field, character type, maximum length of 255, unique constraint
    mail = fields.CharField(max_length=255, description='User email', unique=True)
    # username field, character type, maximum length of 255, unique constraint
    username = fields.CharField(max_length=255, description='Username', unique=True)
    # password field, character type, maximum length of 32
    password = fields.CharField(max_length=32, description='User password')
