from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
# ham __str__ dung de dat ten cac doi tuong khi hien thi trong giao dien admin
class Question (models.Model):
    question_text = models.CharField(max_length=200) # kieu du lieu xau toi da 200 ki tu
    time_pub = models.DateTimeField()
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # CASCADE nghia la khi cau hoi bi xoa thi cau tra loi cung bi xoa
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField(max_length=1000, blank=False, null=False)
    email = models.EmailField(default='default@gmail.com', max_length=255, blank=False, null=False)
    time_create = models.DateTimeField(default=timezone.datetime.now())
    def __str__(self):
        return self.title


# de su dung authen cua abstract user thi can phai cau hinh trong settings.py
class MyUser(AbstractUser):
    gender_choice = ((0, 'female'), (1, 'male'))
    age = models.IntegerField(default=0)
    gender = models.IntegerField(choices=gender_choice, default=0)
    address = models.CharField(default='VN', max_length=255)
