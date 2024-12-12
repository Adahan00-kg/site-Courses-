from django.urls import path
from .views import *

urlpatterns = [
    # FOR STUDENT

    path('student/', StudentListAPIView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentRetrieveUpdateAPIView.as_view(), name='student-detail'),

    path('courses/', CourseStudentListAPIView.as_view(), name='courses-list'),
    path('courses/<int:pk>/', CourseStudentRetrieveAPIView.as_view(), name='courses-detail'),

    path('assignment/', AssignmentListAPIView.as_view(), name='assignment-list'),
    path('assignment/<int:pk>/', AssignmentRetrieveAPIView.as_view(), name='assignment-detail'),
    path('submission/', AssignmentSubmissionListCreateAPIView.as_view(), name='submission-list'),

    path('exam/', ExamListAPIView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamRetrieveAPIView.as_view(), name='exam-detail'),

    path('exam/', ExamListAPIView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamRetrieveAPIView.as_view(), name='exam-detail'),

    path('question/', QuestionListCreateAPIView.as_view(), name='question-list'),

    path('cart/', CartRetrieveAPIView.as_view(), name='cart_detail'),

    path('cart_items/', CartItemListCreateAPIView.as_view(), name='cart_item_list'),
    path('cart_items/<int:pk>/', CartItemRetrieveUpdateDestroyAPIView.as_view(), name='cart_item_detail'),

    path('order/', OrderListCreateAPIView.as_view(), name='order-list'),

    # FOR TEACHER

]
