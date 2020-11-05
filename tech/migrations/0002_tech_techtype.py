# Generated by Django 2.2.5 on 2020-11-05 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tech',
            name='techType',
            field=models.CharField(choices=[('B', 'Back-End'), ('F', 'Front-End')], default=None, max_length=7),
        ),
    ]