# Routing for the basic services

from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('UserRegistration/',CoderRegistraionView.as_view()),
    path('AdminRegistration/',AdminRegistraionView.as_view()),
    path('verify/',ActivateUser),
    path('login/',UserLogin.as_view()),
    path('RestPassword/',RestPassword.as_view()),
    path('RestPasswordToken/',RestPasswordToken.as_view()),
    path('ForgotPassword/',ForgotPassword.as_view()),
    path('EnterQuestion/',EnterQuestion.as_view()),
    path('GetQuestionById/',GetQuestionById.as_view()),
    path('GetAllQuestions/',GetAllQuestions.as_view())
]
