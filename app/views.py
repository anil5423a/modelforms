from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def sunny_web(request):
    TFMO=TopicForm()
    d={'form':TFMO}
    if request.method=='POST':
        FD=TopicForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('inserted success fully')

    return render(request,'sunny_web.html',d)


def insert_webpage(request):
    WFMO=webpageForm()
    d={'form':WFMO}
    if request.method=='POST':
        FD=webpageForm(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('webpage inserted succefully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecords(request):
    ARMO=Accessrecords()
    d={'form':ARMO}
    if request.method=='POST':
        FD=Accessrecords(request.POST)
        if FD.is_valid():
            FD.save()
            return HttpResponse('accessrecords inserted succefully')
    return render(request,'insert_accessrecords.html',d)