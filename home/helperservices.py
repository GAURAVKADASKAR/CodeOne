from home.views import *
from home.models import *
import jwt
from codeone.settings import SECRET_KEY,EMAIL_HOST_USER
from django.core.mail import send_mail
import datetime
from home.serializer import UsersCodingPointsSerializer
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
    "username" : username,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2000)
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


# User activation
def CheackValidToken(token):
    try:
        userdata = jwt.decode(token,SECRET_KEY,algorithms='HS256')
        return userdata['username']
    except jwt.ExpiredSignatureError:
        return False
    except jwt.DecodeError:
        return False

# Check the user verified or not
def CheckUserVerification(username):
    try:
        obj = UserRegistraion.objects.get(username = username).isverified
        return obj
    except UserRegistraion.DoesNotExist:
        return "no username"

# Retrive user type 
def UserType(username):
    obj = UserRegistraion.objects.get(username=username).isadmin
    if obj == True:
        return 'admin'
    else:
        return 'user'

# Check current password
def CheckCurrentPassword(currentpassword,username):
    try:
        user = User.objects.get(username=username)
        obj = user.check_password(currentpassword)
        return obj
    except User.DoesNotExist:
        return False

# Reset password
def ChangePassword(newpassword,username):
    user = User.objects.get(username = username)
    user.set_password(newpassword)
    user.save()

# Send Forgot password token
def SendForgotPasswordToken(email,username):
    token = GenerateToken(username)
    subject="Password Reset for CodeOne"
    message = (
        f"Dear User,\n\n"
        f"Thank you for registering with CodeOne.\n\n"
        f"To complete the registration process and ensure the security of your account, "
        f"please verify your email address by clicking the link below:\n"
        f"https://http://127.0.0.1:8000/ForgotPassword/?token={token}\n\n"
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

# Calculate global ranking function
def CalculateGlobalRankFuntion(username):
    data = UsersCodingPoints.objects.all().order_by("-points")
    serializer = UsersCodingPointsSerializer(data,many=True)
    for i in range (0,len(serializer.data)):
        if serializer.data[i]['username'] == username:
            return i+1
    
def CalculateGlobalLeaderBoard():
    data = UsersCodingPoints.objects.all().order_by("-points")
    serializer = UsersCodingPointsSerializer(data,many=True)
    return serializer.data


# Function to update user points
def UpateUserPoint(username,points,questionlevel,prevpoint,nsq):
    user = UsersCodingPoints.objects.get(username=username)
    user.points -= prevpoint
    user.points += points
    if questionlevel == "Easy":
        user.easyquesitons +=nsq
    elif questionlevel == "Medium":
        user.mediumquesitons +=nsq
    else:
        user.hardquestions +=nsq
    user.solvedquestion +=nsq
    user.save()

def UpadteUserSolvedQuestion(username,question_id,status,points,diffculty):
    question = CodingQuestion.objects.get(id=question_id)
    obj_new  = SolvedQuestion.objects.filter(question_id=question_id)
    if obj_new.exists():
        sp = SolvedQuestion.objects.get(question_id=question_id)
        prevpoint = sp.points
        if sp.points < points:
            sp.points = points
            sp.status = status
            sp.save()
            UpateUserPoint(username,points,diffculty,prevpoint,0)
    else:
        obj = SolvedQuestion.objects.create(
            username = username,
            question_id = question_id,
            status = status,
            difficulty = question.difficulty,
            points = points
        )
        obj.save()
        UpateUserPoint(username,points,diffculty,0,1)



def UpadteSqlQuestion(username,question_id,status,points,diffculty):
    question = CodingQuestion.objects.get(id=question_id)
    obj_new  = SolvedQuestion.objects.filter(question_id=question_id)
    if obj_new.exists():
        sp = SolvedSqlQuestion.objects.get(question_id=question_id)
        prevpoint = sp.points
        if sp.points < points:
            sp.points = points
            sp.status = status
            sp.save()
            UpateUserPoint(username,points,diffculty,prevpoint,0)
    else:
        obj = SolvedQuestion.objects.create(
            username = username,
            question_id = question_id,
            status = status,
            difficulty = question.difficulty,
            points = points
        )
        obj.save()
        UpateUserPoint(username,points,diffculty,0,1)


            



    
    
