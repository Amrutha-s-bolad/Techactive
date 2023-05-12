from datetime import timedelta, datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import *


class GenerateToken(APIView):
    def post(self, request):
        serializer = YourTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh = RefreshToken.for_user(serializer.validated_data['user'])

        token = {
            'access': str(refresh.access_token),
            'expires_in': str(timedelta(minutes=3)),
        }

        return Response(token, status=status.HTTP_200_OK)


request_counts = {}


class InsertUserView(APIView):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        user = request.user

        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email_id = request.POST.get('email_id')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        created_date = datetime.now()

        if not f_name or not l_name or not email_id or not phone_number or not address:
            return JsonResponse({'error': 'One or more required fields missing'}, status=400)

        user_ip = request.META.get('REMOTE_ADDR')
        if user_ip not in request_counts:
            request_counts[user_ip] = [1, datetime.now()]
        else:
            count, last_request_time = request_counts[user_ip]
            time_since_last_request = datetime.now() - last_request_time

            if time_since_last_request > timedelta(minutes=1):
                request_counts[user_ip] = [1, datetime.now()]

            elif count >= 5:
                return JsonResponse({'error': 'Request limit exceeded. Try again after 1 minute.'}, status=429)

            else:
                request_counts[user_ip] = [count + 1, last_request_time]

        try:
            user = User.objects.create(
                f_name=f_name,
                l_name=l_name,
                email_id=email_id,
                phone_number=phone_number,
                address=address,
                created_date=created_date
            )
            user.save()

            return JsonResponse({'message': 'User created successfully'}, status=201)
        except:
            return JsonResponse({'error': 'User creation failed'}, status=500)


def add_user(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        email_id = request.POST.get('email_id')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        user = User(f_name=f_name, l_name=l_name, email_id=email_id, phone_number=phone_number, address=address)
        user.save()

        return JsonResponse({'status': 'success'})

    else:
        return render(request, 'add_form.html')
