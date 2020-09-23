from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo

# Create your views here.
def list_todo_items(request):
    context = {'Todo':Todo.objects.all()}
    return render(request,'todo_app/index.html',context)

def insert_todo_item(request:HttpRequest):
    todo = Todo(content = request.POST['content'])
    todo.save()
    return redirect('/todos/list')