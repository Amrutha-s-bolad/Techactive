from django.contrib.auth import authenticate
from rest_framework import serializers


class YourTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        attrs['user'] = user
        return attrs


'''import requests

url = 'http://127.0.0.1:8002/api/user/'
headers = {'Authorization': f'Bearer {"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgxMzY0NzQ4LCJpYXQiOjE2ODEzNjQ0NDgsImp0aSI6IjFjYTNkYjNjNjgyYjQyMzdiODQzM2FlMzNlOTFiYmIxIiwidXNlcl9pZCI6Mn0.JlJco8nIeLUWal10zd-7cwdUnQWwuJ0Nl1yJ0Rkp0FA"}'}
data = {'f_name': 'John', 'l_name': 'Doe', 'email_id': 'johndoe@example.com', 'phone_number': '1234567890', 'address': '123 Main St.'}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())'''
