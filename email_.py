import os
from dotenv import load_dotenv
import yagmail


def send_email(to: str, email_subject: str, email_body: str, attachment_path: str = None) -> bool:
    """
    Send an email using yagmail.

    Parameters:
    - to (str): The recipient's email address.
    - email_subject (str): The subject of the email.
    - email_body (str): The body of the email.
    - attachment_path (str, optional): The path to the attachment file.

    Returns:
    - bool: True if the email is sent successfully, False otherwise.
    """
    is_sended = False
    try:
        load_dotenv()
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")

        # Create a yagmail SMTP client
        yag = yagmail.SMTP(sender_email, sender_password)

        # Compose the email
        email_contents = [to, email_body]
        if attachment_path:
            email_contents.append(attachment_path)

        # Send the email
        yag.send(to=to, subject=email_subject, contents=email_contents)

        # Close the connection
        yag.close()
        is_sended = True
    except:
        is_sended = False
    finally:
        return is_sended


def is_valid_email(email) -> bool:
    """
    Check if the provided email address has a basic valid format.

    Parameters:
    - email (str): The email address to be validated.

    Returns:
    - bool: True if the email has a basic valid format, False otherwise.
    """
    # Add your email validation logic here
    # For simplicity, let's assume a basic validation for demonstration purposes
    return "@" in email and "." in email
