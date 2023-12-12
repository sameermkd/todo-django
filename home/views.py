from django.shortcuts import render, redirect, HttpResponse
from . forms import TodoForms
from . models import Todo

def home(request):
    form=TodoForms()
    todo=Todo.objects.all()
    context={
        'forms':form,
        'todo':todo
    }
    if request.method=='POST':
        form=TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")       
    return render(request,"index.html",context)
def delete(request,id):
    todo=Todo.objects.get(id=id)
    if request.method=="POST":
        todo.delete()
        return redirect("home")
