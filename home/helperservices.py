from home.views import *
from home.models import *
import jwt
from codeone.settings import SECRET_KEY,EMAIL_HOST_USER
from django.core.mail import send_mail
# services to check wheather the user already exists

def CheckUserNameAvailability(username):
    obj = UserRegistraion.objects.filter(username = username)
    if obj.exists():
        return False
    else:
        return True

# Generate token 
def GenerateToken(username):
    payload = {
    "username" : username
    }
    token = jwt.encode(payload,SECRET_KEY,algorithm='HS256')
    return token

# send email to the user with token
def SendMail(username,email):
    token = GenerateToken(username)
    subject="Account Verification for CodeOne"
    message = (
        f"Dear User,\n\n"
        f"Thank you for registering with CodeOne.\n\n"
        f"To complete the registration process and ensure the security of your account, "
        f"please verify your email address by clicking the link below:\n"
        f"https://http://127.0.0.1:8000/verify/?token={token}\n\n"
        f"If you are unable to click the link above, please copy and paste it into your web browser's address bar.\n\n"
        f"Once your email address has been verified, you will gain full access to our platform and its features.\n\n"
        f"If you did not register with CodeOne, please ignore this email.\n\n"
        f"Thank you for choosing CodeOne. If you have any questions or need further assistance, "
        f"please contact us at CodeOne.support@gmail.com.\n\n"
        f"Best regards,\n"
        f"CodeOne Team"
        )
    from_email = EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,from_email,recipient_list)
