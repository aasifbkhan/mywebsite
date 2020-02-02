from django.contrib import admin

# Register your models here.
from . models import Banner, Profile

admin.site.register(Banner)
admin.site.register(Profile)