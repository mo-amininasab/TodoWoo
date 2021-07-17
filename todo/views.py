from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

class signup_user(View):
    def get(self, request):
        return render(request, 'todo/signupuser.html')
    
    def post(self, request):
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                username = request.POST.get('username')
                password = request.POST.get('username')

                user = User.objects.create_user(username=username, password=password)
                login(request, user)

                return redirect('/current/')
            except IntegrityError:

                return render(request, 'todo/signupuser.html', {'been_taken_error': 'That username had already been taken.'})

        else:
            return render(request, 'todo/signupuser.html', {'not_match_error': 'Passwords did not match.'})

def current_todos(request):
    return render(request, 'todo/currenttodos.html', {})