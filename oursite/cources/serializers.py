from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'student_images', 'grade_level']


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['username', 'student_images', 'grade_level', 'bio_student', 'date_of_birth']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['skills']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class CourseLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLanguages
        fields = ['language', 'video_filed', 'video_url', 'course']


class LessonStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'video_url', 'video_file', 'content']


class CourseStudentListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = ['course_images', 'course_name', 'category', 'description', 'level', 'teacher', 'price',
                  'avg_rating', 'total_people', 'updated_at', 'skills']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()


class CourseStudentDetailSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    course_languages = CourseLanguagesSerializer(read_only=True, many=True)
    category = CategorySerializer()
    skills = SkillsSerializer(read_only=True, many=True)
    lessons = LessonStudentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['course_images', 'course_name', 'category', 'description', 'teacher', 'price', 'avg_rating',
                  'total_people', 'created_at',
                  'updated_at', 'duration', 'skills', 'lessons', 'course_languages']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()


# class AssignmentSimpleSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Assignment
#         fields = ['assignment_name']


class AssignmentSubmissionStudentSerializer(serializers.ModelSerializer):
    students = StudentListSerializer()

    class Meta:
        model = AssignmentSubmission
        fields = ['students', 'course', 'submission_file']


class AssignmentStudentListSerializer(serializers.ModelSerializer):
    students = StudentListSerializer()

    class Meta:
        model = Assignment
        fields = ['students', 'assignment_name', 'description', 'due_date', 'course']


class AssignmentStudentDetailSerializer(serializers.ModelSerializer):
    submissions = AssignmentSubmission()
    students = StudentListSerializer()

    class Meta:
        model = Assignment
        fields = ['students', 'assignment_name', 'description', 'due_date', 'course', 'submissions']


class QuestionSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_name']


class OptionStudentSerializer(serializers.ModelSerializer):
    question = QuestionSimpleSerializer()
    student = StudentListSerializer()

    class Meta:
        model = Option
        fields = ['student', 'question', 'question_choices_student']


class QuestionStudentSerializer(serializers.ModelSerializer):
    option_question = OptionStudentSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['question_name', 'option_question']
        read_only_fields = ['question_name']




class ExamListStudentSerializer(serializers.ModelSerializer):
    course = CourseStudentListSerializer()

    class Meta:
        model = Exam
        fields = ['exam_name', 'course', 'question']


class ExamDetailStudentSerializer(serializers.ModelSerializer):
    question = QuestionStudentSerializer(read_only=True, many=True)
    course = CourseStudentListSerializer()

    class Meta:
        model = Exam
        fields = ['exam_name', 'course', 'passing_score', 'duration', 'question']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url', 'certificate_file']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['student', 'course', 'stars', 'comment', 'created_at']


class CartItemSerializer(serializers.ModelSerializer):
    course = CourseStudentListSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['course', 'total_price']

    def get_total_price(self, obj):
        return obj.get_total_price()


class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    student = StudentListSerializer()
    items = CartItemSerializer(read_only=True, many=True)
    created_date = serializers.DateTimeField(format('%d-%m-%Y-%H:%M'))


    class Meta:
        model = Cart
        fields = ['student', 'items', 'total_price', 'created_date']

    def get_total_price(self, obj):
        return obj.get_total_price()


class OrderSerializer(serializers.ModelSerializer):
    cart_item = CartItemSerializer()
    student = StudentListSerializer()

    class Meta:
        model = Order
        fields = ['student', 'cart', 'status', 'name_on_the_map', 'card_number',
                  'expiration_date', 'cvv', 'country', 'creates_date']


#For Teachers


class TeacherListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'profile_picture', 'years_of_experience']


class TeacherDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username', 'profile_picture', 'bio', 'expertise', 'years_of_experience', 'social_links']


class CourseTeachersListSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    category = CategorySerializer()
    skills = SkillsSerializer()

    class Meta:
        model = Course
        fields = ['teacher', 'course_images', 'course_name', 'category', 'skills', 'description', 'level', 'price',
                  'avg_rating', 'total_people', 'created_at', 'updated_at', 'duration']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()


class CourseTeachersDetailSerializer(serializers.ModelSerializer):
    avg_rating = serializers.SerializerMethodField()
    total_people = serializers.SerializerMethodField()
    course_languages = CourseLanguagesSerializer(read_only=True, many=True)
    category = CategorySerializer()
    skills = SkillsSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['teacher', 'course_images', 'course_name', 'category', 'skills', 'description', 'level', 'price',
                  'avg_rating', 'total_people', 'created_at', 'updated_at', 'duration', 'course_languages']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_total_people(self, obj):
        return obj.get_total_people()


class OptionTeachersSerializer(serializers.ModelSerializer):
    question = QuestionSimpleSerializer()

    class Meta:
        model = Option
        fields = ['teacher', 'question', 'option_choices', 'option', 'option_boolean']


class QuestionTeachersSerializer(serializers.ModelSerializer):
    option_question = OptionStudentSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ['teacher', 'question_name', 'option_question']


class ExamListTeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['teacher', 'exam_name', 'course', 'passing_score', 'duration']


class ExamDetailTeachersSerializer(serializers.ModelSerializer):
    question = QuestionStudentSerializer(read_only=True, many=True)

    class Meta:
        model = Exam
        fields = ['exam_name', 'course', 'passing_score', 'duration', 'question']
