from fastapi import FastAPI

app = FastAPI()


@app.get("/") # define endpoint
async def root():
    return {"message": "Hello World"}


@app.get("/square") # define another endpoint
async def square(num: int):
    result = num ** 2
    return {"squared": result}
