from django.shortcuts import render
from theApp.models import DoubtModel, ClarifyDoubtModel
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from theApp.forms import StudentRegistrationModelForm
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def HomePage(request):

    return render(request,'theApp/HomePage.html')

def RegisterPage(request):

    form = StudentRegistrationModelForm()

    if request.method == 'POST':

        form = StudentRegistrationModelForm(data = request.POST)

        if form.is_valid():

            user = form.save()

            user.set_password(user.password)

            user.save()

            return HomePage(request)

    return render(request,'theApp/RegisterPage.html',{'form':form})

def LoginPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)

        if user:

            login(request,user)

            return HttpResponseRedirect(reverse('homepage'))

        else:

            return render(request,'theApp/LoginPage.html',{'message':'Invalid Details, Please Try Again!'})

    return render(request,'theApp/LoginPage.html')

def AccountPage(request):


    doubts = DoubtModel.objects.all()

    return render(request,'theApp/AccountPage.html',{'doubts':doubts})

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

def ClarifyDoubtPage(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        subject = request.POST.get('subject')
        doubt_pic = request.FILES.get('doubt_pic')
        doubt = request.POST.get('doubt')

        query = ClarifyDoubtModel.objects.create(username = username, subject = subject,doubt_pic = doubt_pic, doubt = doubt)

        query.save()

        return HttpResponseRedirect(reverse('homepage'))

    return render(request,'theApp/ClarifyDoubtPage.html')


def LibraryPage(request):

    return render(request,'theApp/LibraryPage.html')

def LiveClassPage(request):

    return render(request,'theApp/LiveClassPage.html')

@login_required
def Logout(request):

    logout(request)

    return HttpResponseRedirect(reverse('homepage'))
