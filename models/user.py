from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    mobile: str
    address: str
    project_name: str
    deadline: str
    budget: str
    amount_paid: str