from fastapi import FastAPI
from routes import user_api, city_api


app = FastAPI()


@app.get('/')
async def hello_world():
    return "Hello, world!"

app.include_router(
    user_api,
    tags=['user'],
    prefix='/user'
)

app.include_router(
    city_api,
    tags=['city'],
    prefix='/city'
)

