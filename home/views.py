from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from codeone.settings import *
from home.helperservices import UserType,CheckUserNameAvailability,SendMail,CheackValidToken,CheckUserVerification,GenerateToken
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


    

        




