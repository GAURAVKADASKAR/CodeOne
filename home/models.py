from django.db import models
from django.contrib.auth.models import User

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
    solvedquestion = models.PositiveBigIntegerField(default=0)
    mediumquesitons = models.PositiveBigIntegerField(default=0)
    easyquesitons = models.PositiveBigIntegerField(default=0)
    hardquestions = models.PositiveBigIntegerField(default=0)
    globalrank =  models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.username

