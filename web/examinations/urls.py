from django.urls import path

from web.examinations import views

app_name = "examinations"
urlpatterns = [
    path("", views.get_welcome_exam, name="welcome examination"),
    path("<str:examination_id>/result/", views.get_welcome_exam_result, name="examination result"),
]
