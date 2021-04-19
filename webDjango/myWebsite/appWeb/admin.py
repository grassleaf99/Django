from django.contrib import admin
from .models import Choice, Question, Post, MyUser
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Post)
admin.site.register(MyUser)


