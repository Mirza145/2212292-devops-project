from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


class StudentCreate(BaseModel):
    name: str
    reg_no: str


@app.get("/health")
def health_check(db: Session = Depends(database.get_db)):
    try:
        db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"

    return {
        "status": "ok",
        "db": db_status,
        "student": "2212292"
    }


@app.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(database.get_db)):
    db_student = models.Student(name=student.name, reg_no=student.reg_no)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students")
def get_students(db: Session = Depends(database.get_db)):
    return db.query(models.Student).all()


@app.get("/students/{reg_no}")
def get_student(reg_no: str, db: Session = Depends(database.get_db)):
    student = db.query(models.Student).filter(models.Student.reg_no == reg_no).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
