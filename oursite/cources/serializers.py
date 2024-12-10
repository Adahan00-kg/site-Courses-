from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['user', 'profile_picture', 'bio']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'description', 'category', 'level' 'price', 'created_by', 'created_at', 'updated_at', 'course_images']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['course', 'skills']


class CourseLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLanguages
        fields = ['language', 'video_filed', 'video_url', 'course']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'video_file', 'content', 'course']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'students']


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['students', 'assignment', 'submission_file', 'grade']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title_exam', 'course', 'passing_score']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title_question', 'exam']


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['question', 'options_choices', 'options_text']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url', 'certificate_file']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user', 'course', 'stars', 'comment', 'created_at']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user', 'created_date']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'course', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['student', 'cart', 'status', 'creates_date']
