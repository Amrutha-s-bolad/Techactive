from django.urls import path

from .views import GenerateToken, InsertUserView, add_user

urlpatterns = [
    path('token/', GenerateToken.as_view(), name='generate_token'),
    path('user/', InsertUserView.as_view(), name='insert_user'),
    path('add_user/', add_user, name='add_user'),
]
