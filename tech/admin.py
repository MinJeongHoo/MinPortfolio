from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Tech)
class TechAdmin(admin.ModelAdmin):
    pass
