from django.contrib import admin
from .models import projects
from .models import contact_model
# Register your models here.

class mainAdmin(admin.ModelAdmin):
  list_display = ("name", "catagory",)
admin.site.register(projects, mainAdmin,)

