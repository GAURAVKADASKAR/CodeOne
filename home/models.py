from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model for the registration for the user
class UserRegistraion(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    isadmin=models.BooleanField(default=False)
    isuser=models.BooleanField(default=False)
    isactive = models.BooleanField(default=False)
    isverified = models.BooleanField(default=False)
    password = models.TextField()

    def __str__(self):
        return self.username

# Model for the Coding Question
class CodingQuestion(models.Model):
    coding_question=models.CharField(max_length=200)
    title = models.TextField()
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])
    constraints = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.PositiveIntegerField(default=10)

    def __str__(self):
        return self.coding_question


class SampleTestCase(models.Model):
    coding_question = models.ForeignKey(CodingQuestion, on_delete=models.CASCADE, related_name='sample_test_cases')
    input_data = models.TextField()
    expected_output = models.TextField()
    is_public = models.BooleanField(default=True)
    testcasepoint =  models.PositiveIntegerField(default=10)
    def __str__(self):
        return f"TestCase for {self.coding_question.coding_question}"

class BackUpUserRegistraion(models.Model):
    username = models.CharField(max_length=50)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    isadmin=models.BooleanField(default=False)
    isuser=models.BooleanField(default=False)
    isactive = models.BooleanField(default=False)
    isverified = models.BooleanField(default=False)
    password = models.TextField(default='')
    def __str__(self):
        return self.username

class UsersCodingPoints(models.Model):
    username = models.CharField(max_length=200)
    points = models.PositiveBigIntegerField(default=0)
    SolvedCodingQuestion = models.PositiveBigIntegerField(default=0)
    mediumquesitons = models.PositiveBigIntegerField(default=0)
    easyquesitons = models.PositiveBigIntegerField(default=0)
    hardquestions = models.PositiveBigIntegerField(default=0)
    globalrank =  models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username
    

# Model for solved questions
class SolvedQuestion(models.Model):
    username = models.CharField(max_length=200)
    question_id=models.CharField(max_length=200)
    status = models.CharField(max_length=20,default='solved')
    points = models.PositiveBigIntegerField(default=0)
    difficulty = models.CharField(max_length=20,choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])
    def __str__(self):
        return self.username

# Model for sql questions
class SqlQuestions(models.Model):
    Sql_question=models.CharField(max_length=200)
    title = models.TextField()
    description = models.TextField()
    difficulty = models.CharField(max_length=20, choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])
    constraints = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    points = models.PositiveIntegerField(default=10)
    expected_output = models.TextField()

    def __str__(self):
        return self.Sql_question
    
    class Meta:
        db_table = 'student'
    
class EmployeeData(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'employee'

class SolvedSqlQuestion(models.Model):
    username = models.CharField(max_length=200)
    question_id=models.CharField(max_length=200)
    status = models.CharField(max_length=20,default='solved')
    points = models.PositiveBigIntegerField(default=0)
    difficulty = models.CharField(max_length=20,choices=[
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ])
    def __str__(self):
        return self.username


