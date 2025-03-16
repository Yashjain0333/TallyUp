# crud 

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    password: str
    emailid: EmailStr
    phonenumber: str
    first_name: str
    last_name: str
