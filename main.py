from fastapi import FastAPI, Path, Query, status, Request, Form
from fastapi.logger import logger
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import Optional 
from fastapi.middleware.cors import CORSMiddleware

from data import UserDataAttributes

app = FastAPI()

#for connecting with React
origins = {
    "http://localhost:3000",
    "localhost:3000"
}
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
#end of React part
    
datalist = {}
    

#Requests
#Diabetes Analyzer
@app.get("/", tags=["root"])
async def root() -> dict: #returns a dictionary
    return {"Data" : "test"}

#for getting the data and putting into data model, then send
@app.post("/form/", tags=["form"])
async def get_data(highbp: float, highchl: float, chlcheck: float, weight: float, height: float, smoker: float, heartd: float, 
                  physact: float, fruit_vege: float, alch: float, healthcare: float, genhealth: float, menthealth: float, 
                  sex: float, age: float):
    #calculations
    #for body mass index, weight/height^2
    bmi = weight/(height ** 2)
    #age level
    agelvl = 0
    if(age < 18):
        agelvl = 0
    elif(18 <= age and age <= 24):
        agelvl = 1
    elif(25 <= age and age <= 29):
        agelvl = 2
    elif(30 <= age and age <= 34):
        agelvl = 3
    elif(35 <= age and age <= 39):
        agelvl = 4
    elif(40 <= age and age <= 44):
        agelvl = 5
    elif(45 <= age and age <= 49):
        agelvl = 6    
    elif(50 <= age and age <= 54):
        agelvl = 7
    elif(55 <= age and age <= 59):
        agelvl = 8
    elif(60 <= age and age <= 64):
        agelvl = 9
    elif(65 <= age and age <= 69):
        agelvl = 10
    elif(70 <= age and age <= 74):
        agelvl = 11
    elif(75 <= age and age <= 79):
        agelvl = 12
    elif(80 <= age):
        agelvl = 13    
    
    #put fruit_vege twice, one for fruit and one for vege
    userdata = UserDataAttributes(high_bp=highbp, high_chol=highchl, chol_check=chlcheck, bmi=bmi, smoker=smoker, heart_disease=heartd, 
                              physical_activity=physact, fruits=fruit_vege, vegetables=fruit_vege, alcohol=alch, healthcare=healthcare, 
                              gen_health=genhealth, mental_health=menthealth, sex=sex, age=agelvl)
    
    return userdata

#Results
@app.get("/results/", tags=["results"])
async def get_results():
    return {"Results":"Success"}