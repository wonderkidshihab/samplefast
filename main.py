from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def sampleHome():
    return {"data": "This is gonna be a sample home page"}