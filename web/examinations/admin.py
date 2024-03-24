from django.contrib import admin

from web.examinations.models import ExaminationQuestion, Examination

admin.site.register(Examination)
admin.site.register(ExaminationQuestion)
