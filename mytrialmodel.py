from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Colg(BaseModel):
    name:str
    rollnum:int
    dept:str
college = []

@app.get("/num/{id}")
def testv(id:int):
    return{"name":"BAIRAVI","id":id,"dept":"CSE"}

@app.post("/aw")
def addstudent(reqStu:Colg):
    college.append(reqStu.dict())
    return reqStu


@app.delete("/dele")
def delstudent():
    college.pop(-1)
    return "student dismissed"
