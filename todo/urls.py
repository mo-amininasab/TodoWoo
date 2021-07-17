from django.urls import path
from .views import  signup_user

app_name = 'todo'

urlpatterns = [
    # Auth
    path('signup/', signup_user, name='signup_page'),
]