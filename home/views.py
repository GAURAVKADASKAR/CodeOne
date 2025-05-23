from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from codeone.settings import *
from home.helperservices import ResetPassword,UserType,CheckUserNameAvailability,SendMail,CheckCurrentPassword,CheackValidToken,CheckUserVerification,GenerateToken,SendForgotPasswordToken
from home.serializer import UserRegistrationSerilalizer
from home.models import *
from django.contrib.auth import authenticate


# User Registraion view
class CoderRegistraionView(APIView):
    def post(self,request):
        request.data['isadmin'] = False
        request.data['isuser'] = True
        validusername = CheckUserNameAvailability(request.data['username'])
        if validusername == True:
            serializer = UserRegistrationSerilalizer(data=request.data)
            if not serializer.is_valid():
                return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors})
            serializer.save()
            SendMail(request.data['username'],request.data['email'])
            return Response({'status':status.HTTP_200_OK,'message':'success'})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'username is already taken'})



# admin Registration view
class AdminRegistraionView(APIView):
    def post(self,request):
        request.data['isadmin'] = True
        request.data['isuser'] = False
        validusername = CheckUserNameAvailability(request.data['username'])
        if validusername == True:
            serializer = UserRegistrationSerilalizer(data=request.data)
            if not serializer.is_valid():
                return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors})
            serializer.save()
            SendMail(request.data['username'],request.data['email'])
            return Response({'status':status.HTTP_200_OK,'message':'success'})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'username is already taken'})
    
    
# Activate the user
@api_view(["GET"])
def ActivateUser(request):
    token = request.GET.get("token")
    username = CheackValidToken(token)
    if username is False:
        return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'invalid token or expired token'})
    else:
        UserRegistraion.objects.filter(username=username).update(isverified = True)
        return Response({'status':status.HTTP_200_OK,'message':'Account successfully activated'})

# User Login
class UserLogin(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        obj = CheckUserVerification(username)
        if obj == 'no username':
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'invalid username'})
        if obj == False:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'user is not verified'})
        loginobj = authenticate(username=username,password=str(password))
        if loginobj is None:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'invalid user credential'})
        token = GenerateToken(username)
        return Response({'status':status.HTTP_200_OK,'message':'Login successfull','token':token,'usertype':UserType(username)})
    
# Service for reset password though account
class RestPassword(APIView):
    def post(self,request):
        token = request.data['token']
        currentpassword = request.data['currentpassword']
        newpassword = request.data['newpassword']
        username = CheackValidToken(token)
        if username == False:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'invalid token'})
        ispasscorrect = CheckCurrentPassword(currentpassword,username)
        if ispasscorrect == False:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'Please enter the valid current password'})
        ResetPassword(newpassword,username)
        return Response({'status':status.HTTP_200_OK,'message':'password reset successfully'})

# Forgot password services
class ForgotPassword(APIView):
    def post(self,request):
        if (request.data.get('username')):
            try:
                obj= UserRegistraion.objects.get(username = request.data.get('username')).email
                SendForgotPasswordToken(obj,request.data.get('username'))
                return Response({'status':status.HTTP_200_OK,'message':'password reset mail is sent to your registered mail'})
            except UserRegistraion.DoesNotExist:
                return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'Invalid username'})
        if (request.data.get('email')):
            try:
                obj= UserRegistraion.objects.get(email = request.data.get('email')).username
                SendForgotPasswordToken(request.data.get('username'),obj)
                return Response({'status':status.HTTP_200_OK,'message':'password reset mail is sent to your registered mail'})
            except UserRegistraion.DoesNotExist:
                return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'Invalid email'})
    
        
        
        




    

        




