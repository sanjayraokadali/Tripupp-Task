from django.shortcuts import render
from theApp.models import DoubtModel
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def HomePage(request):

    return render(request,'theApp/HomePage.html')

def RegisterPage(request):

    return render(request,'theApp/RegisterPage.html')

def CoursePage(request):

    return render(request,'theApp/CoursePage.html')

def DoubtPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        subject = request.POST.get('subject')
        language = request.POST.get('language')
        doubt = request.POST.get('doubt')

        query = DoubtModel.objects.create(username = username, subject = subject,language = language, doubt = doubt)

        query.save()

        return HomePage(request)

    return render(request,'theApp/DoubtPage.html')

def LibraryPage(request):

    return render(request,'theApp/LibraryPage.html')

def LiveClassPage(request):

    return render(request,'theApp/LiveClassPage.html')
