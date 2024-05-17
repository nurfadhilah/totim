from django.contrib import admin
from .models import Student, Shobby, Mentor

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Shobby)
