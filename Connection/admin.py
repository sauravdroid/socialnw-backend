from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(Request)