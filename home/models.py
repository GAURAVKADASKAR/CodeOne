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
    solvedquestion = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username
    

# Model for solved questions
class SolvedQuestion(models.Model):
    username = models.CharField(max_length=200)
    question_id=models.CharField(max_length=200)
    status = models.CharField(max_length=20,default='solved')
    points = models.PositiveBigIntegerField(default=0)
    user_code = models.TextField(default='')
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
    
# Model for quiz 
class Quiz(models.Model):
    quiz_name=models.CharField(max_length=200)
    title = models.TextField()
    description = models.TextField()
    total_questions = models.PositiveIntegerField(default=10)
    total_marks = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.quiz_name

# Model for quiz questions
class QuizQuestion(models.Model):
    quiz_id = models.CharField(max_length=200)
    quiz_question=models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quiz_question

# Model for quiz answers
class QuizAnswer(models.Model):
    quiz_question_id = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.quiz_question_id

# Model for quiz results
class QuizResult(models.Model):
    username = models.CharField(max_length=200)
    quiz_id = models.CharField(max_length=200)
    score = models.PositiveIntegerField(default=0)
    total_questions = models.PositiveIntegerField(default=0)
    correct_answers = models.PositiveIntegerField(default=0)
    attempted_questions = models.PositiveIntegerField(default=0)
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
# Model for quiz registration
class QuizRegistration(models.Model):
    username = models.CharField(max_length=200)
    quiz_id = models.CharField(max_length=200)
    registration_time = models.DateTimeField(auto_now_add=True)
    is_submitted = models.BooleanField(default=False)
    submission_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.username


# Model for hackathon
class HackaThon(models.Model): 
    hackathon_name=models.CharField(max_length=200)
    email = models.EmailField() 
    organizer_name = models.CharField(max_length=200)
    number_of_teams = models.PositiveIntegerField()
    title = models.TextField()
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    registration_deadline = models.DateTimeField()
    is_registration_open = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    def __str__(self):
        return self.hackathon_name

# Model for hackathon problemStatements
class hackathonProblemStatement(models.Model):
    hackathon_id = models.ForeignKey(HackaThon,on_delete=models.CASCADE)
    subject = models.TextField()
    number_of_team = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    description = models.TextField()
    def __str__(self):
        return str(self.hackathon_id) + " : " + self.subject


# Model for HackaThon registration
class HackaThonRegistration(models.Model):
    PARTICIPATION_TYPE = [
        ('member', 'Member'),
        ('lead', 'Lead'),
    ]
    hackathon_id = models.CharField(max_length=50)
    hackathon_name = models.TextField()
    member_name = models.CharField(max_length=50)
    member_email = models.EmailField()
    member_type = models.CharField(max_length=20,choices=PARTICIPATION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    team_name = models.TextField()
    team_id = models.TextField(null=True,blank=True)
    college_name = models.CharField(max_length=50)
    phone_number = models.TextField()

    def __str__(self):
        return (self.member_name + self.team_name)

# Model for hackathon problem to team
class HackathonProblemTeam(models.Model):
    hackathon_id = models.ForeignKey(HackaThon,on_delete=models.CASCADE)
    problem_statement_id = models.ForeignKey(hackathonProblemStatement,on_delete=models.CASCADE)
    team_id = models.ForeignKey(HackaThonRegistration,on_delete=models.CASCADE)
    
