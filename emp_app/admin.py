from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Role)
admin.site.register(Employe)
admin.site.register(Department)
