from django.urls import path
from . import views
app_name = 'todo'

urlpatterns = [
    # Auth
    path('signup/', views.signup_user.as_view(), name='signup_page'),
    path('logout/', views.logout_user.as_view(), name='logout_page'),
    path('login/', views.login_user.as_view(), name='login_page'),

    # Todos
    path('createtodo/', views.CreateTodo.as_view(), name='create_todo_page'),
    path('current/', views.current_todos.as_view(), name='current_page'),
    path('current/<int:todo_pk>/', views.TodoDetail.as_view(), name='todo_detail_page'),
    path('current/<int:todo_pk>/complete/', views.CompleteTodo.as_view(), name='complete_todo_page'),
    path('current/<int:todo_pk>/delete/', views.DeleteTodo.as_view(), name='delete_todo_page'),
    path('completed/', views.CompletedTodos.as_view(), name='completed_todos_page'),
]