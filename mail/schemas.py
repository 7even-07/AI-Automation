from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict

class Email(BaseModel):
    from_email: str = Field(..., alias="from")
    subject: str
    body: str
    
    class Config:
        populate_by_name = True


class EmailLogCreate(BaseModel):
    prompt: str
    response: str
