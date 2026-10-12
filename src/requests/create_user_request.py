from typing import Optional

from pydantic import BaseModel, Field, field_validator

class CreateUserRequest(BaseModel):
    username: str = Field(default=None, description='Username')
    password: str = Field(default=None, description='Password')
    email: str = Field(default=None, description='Email')
    first_name: str = Field(default=None, description='First name')
    last_name: str = Field(default=None, description='Last name')
    role: str = Field(default=None, description='Role')

    @field_validator('username')
    @classmethod
    def validate_username(cls, v):
        if v is None:
            return None

        assert 5 <= len(v) <= 50

        return v

    @field_validator('password')
    @classmethod
    def validate_password(cls, v):
        if v is None:
            return None

        assert 1 <= len(v) <= 50

        return v

    @field_validator('email')
    @classmethod
    def validate_email(cls, v):
        if v is None:
            return None

        assert 5 <= len(v) <= 50

        return v

    @field_validator('first_name')
    @classmethod
    def validate_first_name(cls, v):
        if v is None:
            return None

        assert 2 <= len(v) <= 50

        return v

    @field_validator('last_name')
    @classmethod
    def validate_last_name(cls, v):
        if v is None:
            return None

        assert 2 <= len(v) <= 50

        return v

    @field_validator('role')
    @classmethod
    def validate_role(cls, v):
        if v is None:
            return None

        assert 3 <= len(v) <= 100
        assert v != 'admin'

        return v