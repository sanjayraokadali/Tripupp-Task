from django.urls import path
from theApp import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'theApp'

urlpatterns = [

    url('^$',views.DoubtPage,name='doubtpage'),
    url('^CoursePage/$',views.CoursePage,name='coursepage'),
    url('^LiveClassPage/$',views.LiveClassPage,name='liveclasspage'),
    url('^LibraryPage/$',views.LibraryPage,name='librarypage'),
    url('^StudentRegistration/$',views.RegisterPage,name='registerpage'),
    url('^ClarifyDoubtPage/$',views.ClarifyDoubtPage,name='clarifydoubtpage'),
    url('^/StudentLogin/$',views.LoginPage,name='loginpage'),
    url('^MyAccount/$',views.AccountPage,name='accountpage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
