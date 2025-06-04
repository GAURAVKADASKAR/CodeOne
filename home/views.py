from home.basemodules import *

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
        ChangePassword(newpassword,username)
        return Response({'status':status.HTTP_200_OK,'message':'password reset successfully'})

# Reset password service
class RestPasswordToken(APIView):
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
        
# Forgot password service
class ForgotPassword(APIView):
    def post(self,request):
        token = request.GET.get('token')
        newpassword = request.data['newpassword']
        username = CheackValidToken(token)
        if username == False:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'Invalid token'})
        ChangePassword(newpassword,username)
        return Response({'status':status.HTTP_200_OK,'message':'password has been changed successfully'})

# Service to insert the coding questions
class EnterQuestion(APIView):
    def post(self,request):
        serializer = CodingQuestionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':serializer.errors})
        serializer.save()
        return Response({'stauts':status.HTTP_200_OK,'message':'success'})

# To fetch Question by id
class GetQuestionById(APIView):
    def post(self,request):
        try:
            id =request.data.get('id')
            question = CodingQuestion.objects.get(id=id)
            sample_test_cases = question.sample_test_cases.filter(is_public=True)
            return Response({
                "Question":{
                "question": question.coding_question,
                "title": question.title,
                "description": question.description,
                "difficulty": question.difficulty,
                "constraints": question.constraints
            },
                "sample_test_cases": [
                    
                    {
                        "input_data": tc.input_data,
                        "expected_output": tc.expected_output
                    } for tc in sample_test_cases
                ]
            })
        except CodingQuestion.DoesNotExist:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'not exists'})
    
# To fetch all the questions
class GetAllQuestions(APIView):
    def get(self,request):
        Questions = CodingQuestion.objects.all()
        question_list=[]
        for Question in Questions:
            sample_test_cases = Question.sample_test_cases.filter(is_public=True)
            question_list.append(
                 {
                "Question":{
                "question": Question.coding_question,
                "title": Question.title,
                "description": Question.description,
                "difficulty": Question.difficulty,
                "constraints": Question.constraints
            },
                "sample_test_cases": [
                    
                    {
                        "input_data": tc.input_data,
                        "expected_output": tc.expected_output
                    } for tc in sample_test_cases
                ]
            }
            )
        return Response({'status':status.HTTP_200_OK,'Questions':question_list,'message':'success'})

# Delete profile (Account)
class DeleteAccount(APIView):
    def post(self,request):
        token = request.data.get('token')
        username = CheackValidToken(token)
        if username == False:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'message':'invalid token'})
        obj = User.objects.get(username = username)
        obj1 = UserRegistraion.objects.get(username=username)
        obj1.delete()
        obj.delete()
        return Response({'status':status.HTTP_200_OK,'message':'Account Delete Successfully'})
        

        

    
        
        
        




    

        




