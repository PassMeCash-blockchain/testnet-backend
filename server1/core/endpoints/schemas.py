from pydantic import BaseModel as BM, Field
from typing import Optional

class RegisterRequestSchema(BM):
    """Registration Schema for creating new user"""
    phone_number : int = Field(description="[Add when path is 'create']")
    password : str = Field(description="[Add when path is 'create'] - Can't be same as email, phone, first name, last name or first and last names combinted", min_length=8, max_length=12)
    path : str = Field(description="For Account creation ['path': 'create'], For Personal Information ['path': 'personal-info'], For Contact Infomation ['path': 'contact-info']")
    first_name : str = Field(description="[Add when path is 'personal-info']")
    last_name : str = Field(description="[Add when path is 'personal-info']")
    dob : str = Field(description="[Add when path is 'personal-info'] Allowed format DD/MM/YYYY, DD-MM-YYYY")
    email : str = Field(description="[Add when path is 'personal-info']")
    state : str = Field(description="[Add when path is 'contact-info']")
    lga : str = Field(description="[Add when path is 'contact-info']")
    address : str = Field(description="[Add when path is 'contact-info']")
    addressAlt : Optional[str] = Field(description="[Add when path is 'contact-info']")





