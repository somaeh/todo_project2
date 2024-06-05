from django.urls import path
from . import views

app_name = 'home_app'
urlpatterns = [
    path('', views.todo_list, name = 'home'),
    path('base', views.base),
    path('detail/<int:todo_id>', views.todo_detail_view, name = 'detail_todos'),
    path('delete/<int:todo_id>', views.delete_todo, name = 'delet_todo'),
    path('create/', views.create_form, name = 'create'),
    path('update/<int:todo_id>', views.update_todo, name = 'update_todo'),
]