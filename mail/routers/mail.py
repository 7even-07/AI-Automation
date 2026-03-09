from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..database import get_db
from typing import List
from ..schemas import EmailLogCreate
from ..import models
from sqlalchemy.orm import Session
from ..repository import mail

router = APIRouter(
    prefix="/mail",
    tags=["mail"]
)

@router.get("/")
def get_email_summarise_response(db: Session = Depends(get_db)):
    return mail.get_summarised_mails_reponse(db)