from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo

######################################################## Authenticate
class signup_user(View):
    def get(self, request):
        return render(request, 'todo/signupuser.html')
    
    def post(self, request):
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                username = request.POST.get('username')
                password = request.POST.get('password1')

                user = User.objects.create_user(username=username, password=password)
                login(request, user)

                return redirect('/current/')
            except IntegrityError:

                return render(request, 'todo/signupuser.html', {'been_taken_error': 'That username had already been taken.'})

        else:
            return render(request, 'todo/signupuser.html', {'not_match_error': 'Passwords did not match.'})


class logout_user(View):
    def post(self, request):
        logout(request)
        return redirect('/login/')


class login_user(View):
    def get(self, request):
        return render(request, 'todo/loginuser.html', {})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate, give a user object or None.
        user = authenticate(request, username=username, password=password)

        if user == None:
            return render(request, 'todo/loginuser.html', {'not_found_user_error': 'User not found.'})

        else:
            login(request, user)
            return redirect('/createtodo/')

########################################################

def current_todos(request):
    todos = Todo.objects.filter(user=request.user, completed_at__isnull=True).order_by('-created_at')

    return render(request, 'todo/currenttodos.html', {'todos': todos})


class create_todo(View):
    def get(self, request):
        return  render(request, 'todo/create_todo.html', {})

    def post(self, request):
        # ??????????????????
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
        except ValueError:
            return  render(request, 'todo/create_todo.html', {'bad_date_error': 'Bad data passed in. Try again.'})

        # form.save()
        # return render(request, 'todo/create_todo.html', {'user': form.is_valid()})
        return redirect('/createtodo/')
