import re

from django.shortcuts import render, get_object_or_404

from web.core.settings import WELCOME_EXAMINATION_TITLE
from web.examinations.models import Examination, ExaminationQuestion


def get_welcome_exam(request):
    examination = get_object_or_404(Examination, title=WELCOME_EXAMINATION_TITLE)
    exam_tasks_list = ExaminationQuestion.objects.filter(examinations=examination, is_active=True)
    return render(request, "welcome_examination.html", {"examination": examination, "questions_list": exam_tasks_list})


def get_welcome_exam_result(request, examination_id: str):
    UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)
    examination = get_object_or_404(Examination, id=examination_id)
    if request.method == "POST":
        result = 0
        for value in request.POST:
            if not bool(UUID_PATTERN.match(value)):
                continue
            question = ExaminationQuestion.objects.get(id=value, is_active=True)
            if question.answer == request.POST.get(value):
                result += 1
        questions = ExaminationQuestion.objects.filter(examinations=examination, is_active=True)
        return render(
            request,
            "welcome_examination_result.html",
            {"examination": examination, "result": int(result/len(questions)*100)}
        )
    else:
        return get_welcome_exam(request)
