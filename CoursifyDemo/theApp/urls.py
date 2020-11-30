from django.urls import path
from theApp import views
from django.conf.urls import url

app_name = 'theApp'

urlpatterns = [

    url('^$',views.DoubtPage,name='doubtpage'),
    url('^CoursePage/$',views.CoursePage,name='coursepage'),
    url('^LiveClassPage/$',views.LiveClassPage,name='liveclasspage'),
    url('^LibraryPage/$',views.LibraryPage,name='librarypage'),
    url('^StudentRegistration/$',views.RegisterPage,name='registerpage'),

]
