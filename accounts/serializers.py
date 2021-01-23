from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    # password2 = serializers.CharField(max_length=24)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }

        def save(self):
            user = User(
                username=self.validated_data['username'],
                email=self.validated_data['email'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name']


            )
            password = self.validated_data['password']
            # password2 = self.validated_data['password2']
            #
            # if password2 != password:
            #     raise ValidationError({'password': 'Password mismatch'})
            # else:
            user.set_password(password)
            user.save()
            return user
