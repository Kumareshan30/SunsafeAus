from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Item
from app.schemas import ItemSchema
from app.ai_model import predict

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fetch all items from PostgreSQL
@router.get("/items", response_model=list[ItemSchema])
def get_items(db: Session = Depends(get_db)):
    return db.query(Item).all()

# AI Prediction Route
@router.get("/predict/{input_value}")
def get_prediction(input_value: float):
    result = predict(input_value)
    return {"prediction": result.tolist()}
