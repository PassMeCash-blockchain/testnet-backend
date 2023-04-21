from pydantic import BaseModel as BM, Field
from typing import Optional

class  PersonalRequestHeaderSchema(BM):
    xPMC : str = Field(title='xPMC',description='',)

class CreateRequestSchema(BM):
    """Registration Schema for creating new user"""
    phone_number : int = Field(description="Phone number]")
    password : str = Field(description="Can't be same as email, phone, first name, last name or first and last names combinted", min_length=8, max_length=12)


class PersonalRequestSchema(BM):
    """Adding Personal Info Schema to a user"""
    first_name : str = Field(description="Users legal First Name")
    last_name : str = Field(description="Users legal Last Name")
    dob : str = Field(description="Allowed format DD/MM/YYYY, DD-MM-YYYY")
    email : str = Field(description="Users Email Address")

class ContactRequestSchema(BM):
    """Adding Contact Info Schema to a user"""
    state : str = Field(description="Users state")
    lga : str = Field(description="Users LGA")
    address : str = Field(description="Users Address")
    addressAlt : Optional[str] = Field(description="Users other address")


class LoginRequestSchema(BM):
    """Authenticating a user"""
    login : str = Field(description="Users Email or Phone number can be passed")
    password : str = Field(description="Users password")


