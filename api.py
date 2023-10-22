from fastapi import FastAPI, Request, Form
from fastapi.middleware.cors import CORSMiddleware

from generate import generate

# Starting the fastapi framework
app = FastAPI()

# For allowing react connections
origins = {
    "http://localhost:3000",
    "localhost:3000"
}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
# End of React part

@app.post("/form/")
async def get_data(request: Request, high_bp: float = 0.0, high_chol: float = 0.0, chol_check: float = 0.0, weight: float = None, height: float = None, smoker: float = 0.0,
                   heart_disease: float = 0.0, physical_activity: float = 0.0, fruit_vege: float = 0.0, alcohol: float = 0.0, stroke: float = 0.0, health_care: float = 1.0,
                   gen_health: float = 3.0, mental_health: float = 3.0, sex: float = 0.0, age: float = 35.0):
    """Diabetes Analyzer, input form data, output evaluation metrics and generated paragraph"""

    # For body mass index, weight/height^2
    if weight is None or height is None:
        bmi = 24
    else:
        bmi = weight / (height ** 2)

    # High cholesterol 240 mg/dL
    high_chol_check = 0
    if(high_chol >= 240):
        high_chol_check = 1
    
    # Age level (13 level metric)
    age_lvl = 0
    if(age < 18):
        age_lvl = 0
    elif(18 <= age and age <= 24):
        age_lvl = 1
    elif(25 <= age and age <= 29):
        age_lvl = 2
    elif(30 <= age and age <= 34):
        age_lvl = 3
    elif(35 <= age and age <= 39):
        age_lvl = 4
    elif(40 <= age and age <= 44):
        age_lvl = 5
    elif(45 <= age and age <= 49):
        age_lvl = 6
    elif(50 <= age and age <= 54):
        age_lvl = 7
    elif(55 <= age and age <= 59):
        age_lvl = 8
    elif(60 <= age and age <= 64):
        age_lvl = 9
    elif(65 <= age and age <= 69):
        age_lvl = 10
    elif(70 <= age and age <= 74):
        age_lvl = 11
    elif(75 <= age and age <= 79):
        age_lvl = 12
    elif(80 <= age):
        age_lvl = 13

    # Fruit/veg consumption is the same field
    user_data = [high_bp, high_chol_check, chol_check, bmi, smoker, heart_disease, physical_activity, fruit_vege, fruit_vege, alcohol, stroke, health_care, gen_health, mental_health, sex, age_lvl]

    #Get generation
    diabetes_pred, adv_paragraph = generate(user_data)

    # Return percentage of the diabetes risk, and a paragraph that tells you what you can do to lessen diabetes/risk of diabetes
    return {
        "diabetes_percent": diabetes_pred, 
        "advice_paragraph": adv_paragraph,
    }
