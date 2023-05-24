"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from . import views

app_name = 'management'
urlpatterns = [
    path('',views.home,name="home"),
    path("student-register/",views.student_register,name="studetn_register"),
    path("teacher-register/",views.teacher_register,name="teacher_register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    
    path("teacher-profile/",views.teacher_profile,name="teacher_profile"),
    path("update-teacher-profile/",views.update_teacher_profile,name="update_teacher_profile"),
    path("create-subject/",views.create_subject,name="create_subject"),
]
