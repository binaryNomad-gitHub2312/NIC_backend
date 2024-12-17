from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello-world/',views.predictor,name='hello_world'),
    path('recommend',views.userInfo),
    path('result',views.formInfo),
    path('hello',views.policyInfo)
]
