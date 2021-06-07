from django.shortcuts import render, redirect
from .models import projects, About
from .forms import ProjectForm, GeeksForm
from django.shortcuts import get_object_or_404
from django.views.generic.edit import DeleteView
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def home(request):
    projs = projects.objects.all()
    abouts = About.objects.all()
    return render(request, 'main.html', {'projs':  projs, 'abouts':abouts})

def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = ProjectForm()

        return render(request, 'form.html', {'form': form})
    else:
        return render(request, 'not.html')



def manage(request):
    if request.user.is_authenticated:
        return render(request, 'manage.html')
    else:
        return render(request, 'not.html')


def table(request):
    if request.user.is_authenticated:
        projs = projects.objects.all()
        return render(request, 'table.html', {'projs':  projs})
    else:
        return render(request, 'not.html')


def detail_view(request, id):
    if request.user.is_authenticated:
        context ={}
        context["data"] = projects.objects.get(id = id)
        return render(request, "detail_view.html", context)
    else:
        return render(request, 'not.html')

def update_view(request, id):
    if request.user.is_authenticated:
        context ={}
        obj = get_object_or_404(projects, id = id)
        form = GeeksForm(request.POST or None, instance = obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/"+id)
        context["form"] = form 
        return render(request, "update_view.html", context)
    else:
        return render(request, 'not.html')

class GeeksDeleteView(DeleteView):
    model = projects
    success_url ="/table"


def login(request):
    return render(request, "registration/login.html")
