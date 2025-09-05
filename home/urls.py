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
    path('GetAllQuestions/',GetAllQuestions.as_view()),
    path('DeleteAccount/',DeleteAccount.as_view()),
    path('GlobalRank/',GlobalRank.as_view()),
    path('GlobalLeaderBoard/',GlobalLeaderBoard.as_view()),
    path('VerifyCodeForTestCase/',VerifyCodeForTestCase.as_view()),
    path('NewsqlQuestion/',EnterSqlQuestion.as_view()),
    path('ExecuteUserSql/',ExecuteUserSql.as_view()),
    path('GetAllSolvedQuestion/',GetAllSolvedQuestion.as_view()),
    path('GetAllSolutionById/',GetAllSolutionById.as_view()),
    path('CreateQuiz/',CreateQuiz.as_view()),
    path('GetAllQuiz/',GetAllQuiz.as_view()),
    path('GetQuizById/',GetQuizById.as_view())
]
