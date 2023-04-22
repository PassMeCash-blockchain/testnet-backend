from pydantic import BaseModel as BM, Field
from typing import Optional
from enum import Enum
import datetime

class Status(str, Enum):
    stepTwo = 'step two'
    stepThree = 'step three'
    complete = 'complete'

class otp(BM):
    sent : Optional[bool]

class Res(BM):
    access: Optional[str]
    refresh : Optional[str]
    registration_stage : Optional[Status] = Status.stepTwo
    otp : Optional[otp]

class CreateUserResponse(BM):
    message : Optional[Res]

class CreateUserBadResponse(BM):
    phone_number : Optional[str] = Field(default='Phone number has been used.')



class Res(BM):
    registration_stage : Optional[Status] = Status.stepThree

class Ress(BM):
    registration_stage : Optional[Status] = Status.complete


class PersonalUserResponse(BM):
    message : Optional[Res] = Field(description='Create Personal Info Response')

class PersonalUserNotFoundResponse(BM):
    user : Optional[str] = Field(default='No user found.', description="xPMC was not passed in the header or token is invalid")

class PersonalUserInternalResponse(BM):
    error : Optional[str]


class ContactUserResponse(BM):
    message : Optional[Ress] = Field(description='Create Contact Info Response')

class ContactUserInternalResponse(BM):
    error : Optional[str]

class ContactUserNotFoundResponse(BM):
    user : Optional[str] = Field(default='No user found.', description="xPMC was not passed in the header or token is invalid")

class UD(BM):
    phone_number : Optional[str]
    dob : Optional[datetime.date]
    state : Optional[str]
    lga : Optional[str]
    address : Optional[str]
    address_alt : Optional[str]
    is_verified : Optional[bool]


class LR(BM):
    refresh : Optional[str]
    access : Optional[str]
    last_login : Optional[datetime.datetime]
    registration_stage : Optional[Status] = Status.complete
    user_details : Optional[UD]
    registration_stage : Optional[str]

class LoginResponse(BM):
    message : Optional[LR] = Field(description='Login Response')


class NotAcceptedLoginResponse(BM):
    message : Optional[str] = Field(description='No account found with the given credentials.')

class ForbiddenLoginResponse(BM):
    error : Optional[str] = Field(description='FORBIDDEN')

class UnauthorizedLoginResponse(BM):
    error : Optional[str] = Field(description='UNAUTHORIZED')

class InternalLoginResponse(BM):
    error : Optional[str]

class NotFoundLoginResponse(BM):
    user : Optional[str] = Field(default='No user found.')
