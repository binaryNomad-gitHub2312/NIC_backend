
from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include

def home_view(request):
    return HttpResponse("Backend is working successfully!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('',include('recommend_App.urls')),
]
