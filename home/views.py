from django.shortcuts import render
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
            return render(request,"index.html",context)        
    return render(request,"index.html",context)
