# Generated by Django 5.0.3 on 2024-03-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examinations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examinationquestion',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
