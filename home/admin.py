from django.contrib import admin
from home.models import *


# Models registration
admin.site.register(UserRegistraion)
admin.site.register(CodingQuestion)
admin.site.register(SampleTestCase)
admin.site.register(BackUpUserRegistraion)
admin.site.register(UsersCodingPoints),
admin.site.register(SolvedQuestion),
admin.site.register(SqlQuestions),
admin.site.register(EmployeeData)
admin.site.register(SolvedSqlQuestion)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)
admin.site.register(QuizResult)
admin.site.register(QuizRegistration)
admin.site.register(HackaThon)
admin.site.register(HackaThonRegistration)
admin.site.register(HackathonProblemTeam)
admin.site.register(hackathonProblemStatement)
admin.site.register(HackathonJudge)
admin.site.register(EvaluationCriteria)
admin.site.register(HackaThonMarks)