from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from codeone.settings import *
from home.helperservices import CheckUserNameAvailability,SendMail
from home.serializer import UserRegistrationSerilalizer

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

