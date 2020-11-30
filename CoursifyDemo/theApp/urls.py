from django.urls import path

app_name = 'theApp'

urlpatterns = [

    path('^$',views.DoubtPage,name='doubtpage'),
    path('^CoursePage/$',views.CoursePage,name='coursepage'),
    path('^LiveClassPage/$',views.LiveClassPage,name='liveclasspage'),
    path('^LibraryPage/$',views.LibraryPage,name='librarypage'),
    
]
