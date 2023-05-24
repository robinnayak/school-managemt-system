from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user.username
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    courses = models.ManyToManyField(Subject)
    section = models.CharField(max_length=1)

    def __str__(self):
        return self.user.username
    

# class Class(models.Model):
#     name = models.CharField(max_length=100)
#     teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
#     students = models.ManyToManyField(Student)
    
#     def __str__(self):
#         return self.name
    
# class Attendance(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
#     date = models.DateField()
#     is_present = models.BooleanField(default=False)

#     def __str__(self):
#         return self.student.name

# class Assignment(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField()
#     file = models.FileField(upload_to='assignment/')
#     is_completed = models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.student.name

# class Exam(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     date = models.DateField()
#     marks_obtained = models.PositiveIntegerField()

#     def __str__(self):
#         return self.subject.name
    

# class Result(models.Model):
#     student = models.ForeignKey(Student,on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
#     marks_obtained = models.PositiveBigIntegerField()
#     total_marks = models.PositiveIntegerField()
#     percentage = models.DecimalField(max_digits=5,decimal_places=2)

#     def calculate_percentage(self):
#         self.percentage = (self.marks_obtained/self.total_marks) * 100

#     def __str__(self):
#         return self.student.name
    

