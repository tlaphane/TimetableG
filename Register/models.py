from django.db import models
from django.urls import reverse


class Courses(models.Model):
    Course_Code = models.CharField(primary_key=True, max_length=100)
    Course_Name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('course', kwargs={'STDN': self.pk})


class RegisteredStd(models.Model):
    Std_no = models.IntegerField()
    Course_code = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Std_no)


class RegisteredStaffs(models.Model):
    Staff_no = models.IntegerField()
    Course_code = models.ForeignKey(Courses, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Staff_no)


class Login(models.Model):
    Std_no = models.ForeignKey(RegisteredStd, on_delete=models.CASCADE)
    Password = models.IntegerField()

    def __str__(self):
        return str(self.Password)
