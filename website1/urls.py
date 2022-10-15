
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Home',views.Home,name='Home'),
    path('Download',views.Download,name='Download'),
    path('Search',views.Search,name='Search'),
]
