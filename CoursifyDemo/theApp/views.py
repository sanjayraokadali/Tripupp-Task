from django.shortcuts import render

# Create your views here.
def HomePage(request):

    return render(request,'theApp/HomePage.html')

def CoursePage(request):

    return render(request,'theApp/CoursePage.html')

def DoubtPage(request):

    return render(request,'theApp/DoubtPage.html')

def LibraryPage(request):

    return render(request,'theApp/LibraryPage.html')

def LiveClassPage(request):

    return render(request,'theApp/LiveClassPage.html')
