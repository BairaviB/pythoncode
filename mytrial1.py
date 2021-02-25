from fastapi import FastAPI

app = FastAPI()

@app.get("/")

def test():
    return{"name":"BAIRAVI"}

@app.get("/t")

def testq():
    return{"vadivel":"AHAAN"}


@app.get("/num/{id}")

def testv(id:int):
    return{"name":"BAIRAVI","id":id,"dept":"CSE"}
