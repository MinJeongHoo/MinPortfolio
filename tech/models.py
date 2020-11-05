from django.db import models

# Create your models here.


class Tech(models.Model):
    TECH_LOW = "L"
    TECH_MID = "M"
    TECH_HIGH = "H"
    techLevelType = [
        (TECH_LOW, "Low"),
        (TECH_MID, "Middle"),
        (TECH_HIGH, "High")
    ]

    TECH_TYPE1 = "B"
    TECH_TYPE2 = "F"

    techTypeBF = [
        (TECH_TYPE1, "Back-End"),
        (TECH_TYPE2, "Front-End")
    ]

    techType = models.CharField(default=None, max_length=7, choices=techTypeBF)
    techimg = models.ImageField()
    techLevel = models.CharField(max_length=6, choices=techLevelType)
    techName = models.CharField(max_length=20)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
