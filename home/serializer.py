from rest_framework.serializers import ModelSerializer
from home.models import *

# Serializer for the user registraion
class UserRegistrationSerilalizer(ModelSerializer):
    class Meta:
        model = UserRegistraion
        fields = "__all__"

    # Function to create a user
    def create(self, validated_data):
        firstname = validated_data['firstname']
        lastname = validated_data['lastname']
        username = validated_data['username']
        password = validated_data['password']
        isadmin = validated_data['isadmin']
        isuser = validated_data['isuser']
        email = validated_data['email']

        obj = User.objects.create(
            username = username
        )
        obj.set_password(password)
        obj.save()

        userobj = UserRegistraion.objects.create(
            username = username,
            firstname = firstname,
            lastname = lastname,
            isadmin = isadmin,
            isuser = isuser,
            email = email
        )
        userobj.save()
        return validated_data

# Serializer for sampletestcases
class SampleTestCaseSerializer(ModelSerializer):
    class Meta:
        model = SampleTestCase
        fields = ['id', 'input_data', 'expected_output', 'is_public','testcasepoint']
    

# Serializer for the CodingQuestion
class CodingQuestionSerializer(ModelSerializer):
    sample_test_cases = SampleTestCaseSerializer(many=True)
    class Meta:
        model = CodingQuestion
        fields = "__all__"
    
    def create(self, validated_data):
        sample_cases = validated_data.pop('sample_test_cases')
        obj = CodingQuestion.objects.create(**validated_data)
        for sample in sample_cases:
            obj1 = SampleTestCase.objects.create(coding_question = obj , **sample)
        return obj


class UsersCodingPointsSerializer(ModelSerializer):
    class Meta:
        model = UsersCodingPoints
        fields = "__all__"


# Serializer for Sql Question
class SqlQuestionsSerializer(ModelSerializer):
    class Meta:
        model = SqlQuestions
        fields = "__all__"
        
# Serializer for solved coding questions
class SolvedQuestionSerializer(ModelSerializer):
    class Meta:
        model = SolvedQuestion
        fields = "__all__"
    
