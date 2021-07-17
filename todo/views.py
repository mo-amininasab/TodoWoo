import django
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup_user(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm})

    elif request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password1'):
            username = request.POST.get('username')
            password = request.POST.get('username')
            
            User.objects.create_user(username=username, password=password)
           
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm})
