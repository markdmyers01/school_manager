from fastapi import FastAPI, APIRouter
from routes import school_routes

app = FastAPI(
    title='Sample Course Database',
    description='A sample alternative to Flask, using FastAPI'
)

app.include_router(school_routes.router)

# Need to start server from terminal using the following code:
# uvicorn main:app --reload


@app.get("/", tags=['home'])
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}", tags=['home'])
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
