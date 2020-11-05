from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    """ProjectAdmin Definition"""

    """추가시 나오는 필드 구성"""
    fieldsets = (("Project Info", {'fields': ("user",
        "projectname", "company", "projectType", "projectSdate", "projectEdate")}), ("Project Detail", {'fields': ("projectdetail",)}))

    """admin list page 목록 만들기"""
    list_display = ("projectname", "company", "projectSdate", "projectEdate")
