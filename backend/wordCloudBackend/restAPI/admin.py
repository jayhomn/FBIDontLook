from django.contrib import admin
from .models import Hero, UserProfile, CourseName


# Register your models here.
admin.site.register(Hero)
admin.site.register(UserProfile)
admin.site.register(CourseName)