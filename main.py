from fastapi import FastAPI, Request, Form
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError 
from fastapi.middleware.cors import CORSMiddleware

#from the project folder
from model import predict

#starting the fastapi framework
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

#Diabetes Analyzer
#for getting the data and putting into data model, then send
@app.post("/form/", tags=["form"])
async def get_data(request: Request, high_bp: float = Form(0), high_chol: float = Form(0), chol_check: float = Form(0), weight: float = Form(None), height: float = Form(None), smoker: float = Form(0),
                   heart_disease: float = Form(0), physical_activity: float = Form(0), fruit_vege: float = Form(0), alcohol: float = Form(0), stroke:float = Form(0), health_care: float = Form(1),
                   gen_health: float = Form(3), mental_health: float = Form(3), sex: float = Form(0), age: float = Form(35)):
    #calculations
    #for body mass index, weight/height^2
    if weight is None or height is None:
        bmi = 24
    else:
        bmi = weight/(height ** 2)
    
    #high cholesteral 240 mg/dL
    high_chol_check = 0
    if(high_chol >= 240):
        high_chol_check = 1
    
    #age level
    age_lvl = 0
    if(age < 18):
        age_lvl = 0
    elif(18 <= age and age <= 24):
        age_lvl = 1
    elif(25 <= age and age <= 29):
        age_lvl = 2
    elif(30 <= age and age <= 34):
        age_lv = 3
    elif(35 <= age and age <= 39):
        age_lv = 4
    elif(40 <= age and age <= 44):
        age_lv = 5
    elif(45 <= age and age <= 49):
        age_lv = 6    
    elif(50 <= age and age <= 54):
        age_lv = 7
    elif(55 <= age and age <= 59):
        age_lv = 8
    elif(60 <= age and age <= 64):
        age_lv = 9
    elif(65 <= age and age <= 69):
        age_lv = 10
    elif(70 <= age and age <= 74):
        age_lv = 11
    elif(75 <= age and age <= 79):
        age_lv = 12
    elif(80 <= age):
        age_lv = 13    
    
    #put fruit_vege twice, one for fruit and one for vege
    #userdata = UserDataAttributes(high_bp=highbp, high_chol=highchl, chol_check=chlcheck, bmi=bmi, smoker=smoker, heart_disease=heartd, 
                              #physical_activity=physact, fruits=fruit_vege, vegetables=fruit_vege, alcohol=alch, stroke=stroke, healthcare=healthcare, 
                              #gen_health=genhealth, mental_health=menthealth, sex=sex, age=agelvl)
    user_data = [high_bp, high_chol_check, chol_check, bmi, smoker, heart_disease, physical_activity, fruit_vege, fruit_vege, alcohol, stroke, health_care, gen_health, mental_health, sex, age_lv]
    
    #Send to the model
    #input data into the ai
    diabetes_pred, adv_paragraph= predict.generate(user_data)
    #results is a percentage od the diabetes risk, and a paragraph that tells you what you can do to lessen diabetes/risk of diabetes
    
    return diabetes_pred, adv_paragraph

