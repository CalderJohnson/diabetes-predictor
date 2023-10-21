from pydantic import BaseModel
from typing import Optional 

#Data model to be retrieved
class UserDataAttributes(BaseModel):
    high_bp: float
    high_chol: float
    chol_check: float
    bmi: float
    smoker: float
    heart_disease: float
    physical_activity: float
    fruits: float
    vegetables: float
    alcohol: float
    stroke: float
    healthcare: float
    gen_health: float
    mental_health: float
    sex: float
    age: float
    
    
class UpdateUserDataAttributes(BaseModel):
    Name: Optional[str] = None