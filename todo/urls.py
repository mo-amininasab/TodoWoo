from django.urls import path
from .views import  signup_user, current_todos, logout_user, login_user

app_name = 'todo'

urlpatterns = [
    # Auth
    path('signup/', signup_user.as_view(), name='signup_page'),
    path('logout/', logout_user.as_view(), name='logout_page'),
    path('login/', login_user.as_view(), name='login_page'),

    # Todos
    path('current/', current_todos, name='current_page'),
]