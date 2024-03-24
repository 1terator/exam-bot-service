from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Examination(models.Model):
    class ExaminationType(models.TextChoices):
        RUSSIAN = "Russian", _("Russian")

    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    title = models.TextField(max_length=128, db_index=True, unique=True)
    text = models.TextField(max_length=2048, blank=True, null=True)
    type = models.CharField(max_length=128, choices=ExaminationType, db_index=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return f"{self.title}... {self.id}"


class ExaminationQuestion(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid4, editable=False)
    code = models.CharField(max_length=4, null=True, blank=True)
    title = models.TextField(max_length=1024)
    condition = models.TextField(max_length=2048, null=True, blank=True)
    text = models.TextField(max_length=2048, null=True, blank=True)
    answer = models.CharField(max_length=2048)

    examinations = models.ManyToManyField(Examination)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return f"{self.title}... {self.id}"
