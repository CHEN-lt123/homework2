"""
URL configuration for homework2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('homework2/<str:username>/',views.homework2),
    path('lotto1/',views.lotto1),
    path('lotto2/',views.lotto2),

    path('index/',views.index),


    path('',views.index2),

    path('index2/',views.index2),
    path('appointment/', views.appointment_view, name='appointment'),
    path('select-department/', views.select_department_view, name='select_department'),



    path('current_number/', views.current_number, name='current_number'),
    path('lcd_control/', views.lcd_control, name='lcd_control'),
    path('increase_button/', views.increase_button, name='increase_button'),
    path('increase_forESP8266/',views.increase_forESP8266,name='increase_forESP8266'),
    path('clear_number/',views.clear_number,name='clear_number'),
    
    
   
]
