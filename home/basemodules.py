from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from codeone.settings import *
from home.helperservices import UpadteUserSolvedQuestion,UpadteSqlQuestion,UpateUserPoint,CalculateGlobalLeaderBoard,CalculateGlobalRankFuntion,ChangePassword,UserType,CheckUserNameAvailability,SendMail,CheckCurrentPassword,CheackValidToken,CheckUserVerification,GenerateToken,SendForgotPasswordToken
from home.serializer import UserRegistrationSerilalizer,CodingQuestionSerializer,SqlQuestionsSerializer
from home.models import *
from django.contrib.auth import authenticate
from home.compiler import *
from django.db import connection
import json