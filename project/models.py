from django.db import models
import users

# Create your models here.


class Project(models.Model):
    SIDE_PROJECT = 'S'
    MAIN_PROJECT = 'M'
    project_choice = [
        (SIDE_PROJECT, "SIDE_PROJECT"),
        (MAIN_PROJECT, "MAIN_PROJECT")
    ]

    projectname = models.CharField(max_length=20)
    company = models.CharField(max_length=10)
    projectdetail = models.TextField(max_length=1000)
    projectType = models.CharField(max_length=3, choices=project_choice)
    projectSdate = models.DateField()
    projectEdate = models.DateField()
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, default=None, related_name="project")
