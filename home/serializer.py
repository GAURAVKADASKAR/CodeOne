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
    

        