from django.urls import path
from .views import  signup_user, current_todos

app_name = 'todo'

urlpatterns = [
    # Auth
    path('signup/', signup_user.as_view(), name='signup_page'),

    # Todos
    path('current/', current_todos, name='current_page'),
]