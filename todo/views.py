from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import TodoForm
from .models import Todo
from django.utils import timezone

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

                return redirect('/createtodo/')
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

class CompletedTodos(View):
    def get(self, request):
        todos = Todo.objects.filter(user=request.user, completed_at__isnull=False).order_by('-created_at')

        return render(request, 'todo/completed_todos.html', {'todos': todos})

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

class TodoDetail(View):
    def get(self, request, todo_pk):
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        
        return render(request, 'todo/todo_detail.html', {'todo': todo})
    
    def post(self, request, todo_pk):
        todo = Todo.objects.get(pk=todo_pk)
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            # instead of the code down below, use the code up here.
            # if form.is_valid():
            #     todo.title = form.cleaned_data['title']
            #     todo.memo = form.cleaned_data['memo']
            #     todo.important = form.cleaned_data['important']
            #     todo.save()
                
        except ValueError:
            return  render(request, 'todo/todo_detail.html', {'todo': todo, 'bad_date_error': 'Bad data passed in. Try again.'})

        return redirect('/current/')

class CompleteTodo(View):
    def post(self, request, todo_pk):
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.completed_at = timezone.now()
        todo.save()

        return redirect('/current/')

class DeleteTodo(View):
    def post(self, request, todo_pk):
        todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
        todo.delete()

        return redirect('/current/')

