from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE
@app.post("/transactions")
def create_transaction(data: schemas.TransactionCreate, db: Session = Depends(get_db)):
    transaction = models.Transaction(**data.dict())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

# READ
@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()

# UPDATE
@app.put("/transactions/{id}")
def update_transaction(id: int, amount: float, db: Session = Depends(get_db)):
    t = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Not found")
    t.amount = amount
    db.commit()
    return t

# DELETE
@app.delete("/transactions/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    t = db.query(models.Transaction).filter(models.Transaction.id == id).first()
    if not t:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(t)
    db.commit()
    return {"msg": "Deleted"}

# FILTER
@app.get("/transactions/filter")
def filter_transactions(type: str = None, category: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Transaction)
    if type:
        query = query.filter(models.Transaction.type == type)
    if category:
        query = query.filter(models.Transaction.category == category)
    return query.all()

# SUMMARY
@app.get("/summary")
def summary(db: Session = Depends(get_db)):
    data = db.query(models.Transaction).all()
    income = sum(t.amount for t in data if t.type == "income")
    expense = sum(t.amount for t in data if t.type == "expense")

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }

@app.get("/")
def home():
    return {"message": "Finance API is running 🚀"}