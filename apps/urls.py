from django.urls import path

from apps.views import exam_view, exam_detail_view

urlpatterns = [
    path('', exam_view, name='exam_page'),
    path('exam_detail/<int:id>/', exam_detail_view, name='exam_detail_page')
]
