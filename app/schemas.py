from pydantic import BaseModel
from pydantic import BaseModel
from enum import Enum

# limits the user roles to three options: student, alumni, and faculty
class UserRole(str, Enum):
    student = "student"
    alumni = "alumni"
    faculty = "faculty"

# requests validation on creating a new user (requiring an email and password)
class CreateUser(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    role: UserRole = UserRole.student  # default role is student
    notifications: bool = False  # default value for notifications is False

# used for response formatting when returning user data (excluding the password)
class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: UserRole

    class Config:
        # allows to work with SQLAlchemy object relational models
        orm_mode = True

# requests validation on creating a new event (requiring a name, description, location, date, time, student/alumni/faculty, and food availability)
class CreateEvent(BaseModel):
    name: str
    description: str
    location: str
    date: str
    time: str
    student_alumni_prof: str  # indicates if the event is for students, alumni, or faculty
    food_available: str

# used for response formatting when returning event data
class EventResponse(BaseModel):
    id: int
    name: str

    class Config:
        # allows to work with SQLAlchemy object relational models
        orm_mode = True

# used for formatting request when logining in a user
class LoginUser(BaseModel):
    email: str
    password: str