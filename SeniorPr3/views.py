
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .forms import FileForm, AddFile
from .models import data, rawdata
from django.http import HttpResponse, Http404
# Create your views here.

#VIEW INFO IN DATASET
def index(request):
    z = data.objects.all()
    zd = { "info":z }
    return render(request, 'reading/index.html', zd)
  
 ##VIEW TO VIEW DATA IN PDF FILE IMPLEMENT LATER 
  ##      with open('LEADSFINAL2.csv', 'rb') as pdf:
        ###with open('static/finalpics/', 'rb') as pdf:
    #        response = HttpResponse(pdf.read(),content_type='application/pdf')
     #       response['Content-Disposition'] = 'filename=some_file.pdf'
      #      return response

##BUTTON FOR INDIVIDUAL EDITING
def home(request):
    if request.method =="POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:
        form = FileForm()
    return render(request, 'reading/home.html', {
        'form':form
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('reading/register.html')
    else:
        form = UserCreationForm
    info = {
        'form': form
    }
    return render(request, 'reading/register.html', info)

##Adds file to database for later refrence 
def addfile(request):
    if request.method =="POST":
        form = AddFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return redirect('index')
    else:
        form = AddFile()
    return render(request, 'reading/addfile.html', {
        'form':form
    })



