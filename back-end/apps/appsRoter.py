from fastapi import APIRouter
from .user.user import userApi
from .adapter.adapter import adapterApi

# Create an instance of the APIRouter class
api = APIRouter()

# Import the user module routes
api.include_router(userApi, prefix="/user")

# Import the bus-related module routes
api.include_router(adapterApi, prefix="/bus")