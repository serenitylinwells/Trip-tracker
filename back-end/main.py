from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from apps.appsRoter import api
from apps.orm.settings import TORTOISE_ORM

# Create a FastAPI instance
app = FastAPI()

# Once fastapi runs, register_tortoise monitors the app
register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)

# Set up cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Import routes
app.include_router(api, prefix="/api", tags=["app interface collections"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000)
