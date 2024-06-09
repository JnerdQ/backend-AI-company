from typing import Dict
from pydantic import BaseModel


class EmployeeBase(BaseModel):
    name: str
    last_name: str
    email: str
    position: str
    age: int
    is_active: bool
    skills: Dict[str, int]

class EmployeeCreate(EmployeeBase):
    password: str
    
class EmployeeAuthenticate(BaseModel):
    email: str
    password: str

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
