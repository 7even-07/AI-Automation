import imaplib
import email
from keys import EMAIL_ADDRESS, EMAIL_PASSWORD

def fetch_recent_emails(limit=5):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    mail.select("inbox")

    status, response = mail.search(None, "ALL")
    msg_nums = response[0].split()

    latest_emails = msg_nums[-limit:]

    email_data = {}

    for e_id in latest_emails:
        status, msg_data = mail.fetch(e_id, "RFC822")

        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                subject = msg["subject"]
                from_ = msg["from"]

                if msg.is_multipart():
                    body = ""
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode(errors="ignore")
                            break
                else:
                    body = msg.get_payload(decode=True).decode(errors="ignore")

                email_data[e_id.decode()] = {
                    "id": e_id.decode(),
                    "from": from_,
                    "subject": subject,
                    "body": body,
                }

    mail.logout()
    return email_data