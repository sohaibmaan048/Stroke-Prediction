from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from inference import engine

app = FastAPI(title="Stroke Prediction API")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class StrokeInput(BaseModel):
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    ever_married: str
    work_type: str
    Residence_type: str
    avg_glucose_level: float
    bmi: float
    smoking_status: str


@app.get("/", response_class=HTMLResponse)        # ← changed: now serves index.html
def home(request: Request):
   # NEW
   return templates.TemplateResponse(request, "index.html")


@app.post("/predict")                             # ← unchanged
def predict(data: StrokeInput):
    result = engine.predict(data.model_dump())
    return result