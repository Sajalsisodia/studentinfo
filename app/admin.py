from django.contrib import admin
from .models import Students
# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display =  ['id','name','roll','city']