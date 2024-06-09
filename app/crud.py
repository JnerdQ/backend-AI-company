import bcrypt
from app.schemas import Employee, EmployeeCreate
from app.models import Employee as EmployeeModel
from sqlalchemy.orm import Session



def get_employee(db: Session, employee_id: int):
    return db.query(EmployeeModel).filter(EmployeeModel.id == employee_id).first()

def get_employees(db: Session, skip: int = 0):
    return db.query(EmployeeModel).offset(skip).all()

def get_employee_by_email(db: Session, email: str):
    return db.query(EmployeeModel).filter(EmployeeModel.email == email).first()


def create_employee(db: Session, employee: EmployeeCreate):
    hashed_password = bcrypt.hashpw(employee.password.encode('utf-8'), bcrypt.gensalt())
    db_employee = EmployeeModel(
        name=employee.name,
        last_name=employee.last_name,
        email=employee.email,
        position=employee.position,
        age=employee.age,
        hashed_password=hashed_password.decode('utf-8'),
        skills=employee.skills,
        is_active=employee.is_active
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete_all_employees(db: Session):
    db.query(EmployeeModel).delete()
    db.commit()
    

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def authenticate_employee(db: Session, email: str, password: str):
    user = get_employee_by_email(db, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
