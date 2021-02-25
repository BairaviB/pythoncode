from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def func():
    return"welcome to first page"

@app.get("/a")

def funca():
    return"welcome to second page route a"

@app.get("/last")

def funcb():
    return"nandri meedum sandhipom"


