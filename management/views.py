from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import Group,AnonymousUser
from management.forms import *
from management.models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def home(request):
    return HttpResponse("hello world")

# ============ authentication part ==============
def student_register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            student_group = Group.objects.get(name="student")
            user.groups.add(student_group)
            user.save()
            Student.objects.create(user=user,email=user.email)            
            return redirect('management:login')
    
    context = {"form":form}
    return render(request,"register.html",context)

def teacher_register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            teacher_group = Group.objects.get(name="teacher")
            user.groups.add(teacher_group)
            user.save()
            Teacher.objects.create(user=user,email=user.email)            
            return redirect('management:login')
    
    context = {"form":form}
    return render(request,"register.html",context)

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            # print("user:",user.groups.all())
            login(request,user)
            if (str(user.groups.all()[0])=="student"):
                print("render student page")
                return render(request,'student/student_profile.html')
            elif(str(user.groups.all()[0])=="teacher"):
                print("render teacher page")
                return redirect('management:teacher_profile')
        else:
            return HttpResponse("user credential not match")
    context = {}
    return render(request,"login.html",context)

def logout_page(request):
    logout(request)
    return redirect('management:login')

def reset_password(request):
    pass

def forgot_password(request):
    pass

# ================ student page ===================

def teacher_profile(request):
    if request.user.is_authenticated:
        if not isinstance(request.user,AnonymousUser):
            teacher_obj = Teacher.objects.get(email=request.user.email)
            print("teacher obj",teacher_obj)
            context = {"teacher":teacher_obj}
            return render(request,"teacher/teacher_profile.html",context)
    return redirect('management:login')

def update_teacher_profile(request):
    if request.user.is_authenticated:
        user_email = request.user.email
        if request.user is not None:
            if not isinstance(request.user,AnonymousUser):
                teacher_query = Teacher.objects.get(email=user_email)
                form = TeacherForm(instance=teacher_query)
                if request.method == "POST":
                    form = TeacherForm(request.POST,request.FILES,instance=teacher_query)
                    if form.is_valid():
                        form.save()
                        return redirect('management:teacher_profile')
                else:
                    context = {"form":form}
                    return render(request,'teacher/update.html',context)
            return redirect('management:login')
    else:
        return redirect("management:login")

def create_subject(request):
    form = SubjectForm()
    context = {"form":form}
    return render(request,"subject.html",context)