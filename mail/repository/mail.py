from fastapi import HTTPException, status, Response
from sqlalchemy.orm import Session
from ..models import EmailLog
from ..schemas import EmailLogCreate
from .get_mails import fetch_recent_emails
from cerebras_api import email_summarize

MAX_BODY_LENGTH = 4000

def get_summarised_mails_reponse(db: Session):
    emails = fetch_recent_emails(5)
    new_list = []

    for email_id, data in emails.items():
        email_dict = {
            "email_id": email_id,
            "from": data["from"],
            "subject": data["subject"],
            "body": data["body"],
        }
        new_list.append(email_dict)
    all_email_text = ""

    for email_data in new_list:
        all_email_text += f"""
            Email Id: {email_data["email_id"]}
            From: {email_data["from"]}
            Subject: {email_data["subject"]},
            Body: {email_data["body"][:MAX_BODY_LENGTH]}
            -------------------------
        """
    prompt = f"""
                Summarize each email seperately and label them by Email Id:

                {all_email_text}
            """
    # get the response from llm
    response_text = email_summarize(prompt)

    # the db part
    db_log = EmailLog(
        prompt=prompt,
        response=response_text
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    return response_text