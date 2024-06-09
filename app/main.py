# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine 
import app.models as models
import app.crud as crud
import app.schemas as schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app = FastAPI()

# Dependency db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Employee API"}

#Create Employee
@app.post("/employee/", response_model=schemas.Employee, tags=["employee"])
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee_by_email(db, email=employee.email)
    if db_employee:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_employee(db=db, employee=employee)


# Get all employees
@app.get("/employee/", response_model=list[schemas.Employee], tags=["employee"])
def read_employees(db: Session = Depends(get_db)):
    employees = crud.get_employees(db)
    return employees if employees else []

# Get employee by id
@app.get("/employee/{employee_id}", response_model=schemas.Employee, tags=["employee"])
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


# authenticate employee
@app.post("/employee/authenticate", response_model=schemas.Employee, tags=["employee"])
def authenticate_employee(auth_data: schemas.EmployeeAuthenticate, db: Session = Depends(get_db)):
    db_employee = crud.authenticate_employee(db, email=auth_data.email, password=auth_data.password)
    if db_employee is None:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return db_employee

#delete employee by id
@app.delete("/employee/{employee_id}", tags=["employee"])
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, employee_id=employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    crud.delete_employee(db, employee_id=employee_id)
    return {"message": "Employee deleted successfully"}

"""
# delete all employees
@app.delete("/employees/", tags=["employee"])
def delete_all_employees(db: Session = Depends(get_db)):
    crud.delete_all_employees(db)
    return {"message": "All employees have been deleted"}
"""