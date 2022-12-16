from django.shortcuts import render
from django.http import HttpResponse
from .models import *

roles = [
    {'id':1,'role': "admin"},
    {'id':2,'role': "auditor"},
    {'id':3,'role': "subcontractor"},
]

def home(request):
    context={'roles':roles}
    return render(request,'home.html',context)

def adminPage(request):
    acts = Act.objects.all()
    context={'acts':acts}
    if (request.method == 'POST'):
        act_name = request.POST['actn']
        act_desc = request.POST['actd']
        act_sname = request.POST['actsn']
        actsdata = Act.objects.create(act_name = act_name, act_shname = act_sname,description=act_desc)
        actsdata.save()
        acts = Act.objects.all()
        context={'acts':acts}
        return render(request,'adminPage.html',context)
    else:
        return render(request,'adminPage.html',context) 
    
    


def audPage(request):
    get_files = UploadFile.objects.all()
    context={'files':get_files}
    return render(request,'audPage.html',context)

def subPage(request):
    if request.method == "POST":
        filename = request.POST.get('filename')
        files = request.FILES.get('upload')
        new_file = UploadFile.objects.create(f_name = filename,f_file=files)
        new_file.save()
    context={'roles':roles}
    return render(request,'subPage.html',context)

def room(request,pk):
    room = 1
    for i in roles:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    print(context)
    return render(request,'room.html',context)