from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    def __str__(self):
        return self.username


class Teacher(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class Student(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'beginner'),
        ('intermediate', 'intermediate'),
        ('advanced', 'advanced'),
    )
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_images = models.ImageField(upload_to='course_images/')
    DURATION_CHOICES = (
        ('Менее 2 часов', 'Менее 2 часов'),
        ('1–4 недели', '1–4 недели'),
        ('1–3 месяца', '1–3 месяца'),
        ('3–6 месяцев', '3–6 месяцев'),

    )
    duration = models.CharField(max_length=40, choices=DURATION_CHOICES)

    def __str__(self):
        return self.course_name

    class Meta:
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['created_by']),
            models.Index(fields=['level']),
        ]

    def get_avg_rating(self):
        ratings = self.reviews.all()
        if ratings.exists():
            return round(sum(i.stars for i in ratings) / ratings.count(), 1)
        return 0

    def get_total_people(self):
        ratings = self.reviews.all()
        if ratings.exists():
            if ratings.count() > 10000:
                return '10000+'
            return ratings.count()
        return 0


class Skills(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='skills')
    skills = models.CharField(max_length=155, null=True, blank=True)


class CourseLanguages(models.Model):
    language = models.CharField(max_length=35)
    video_filed = models.FileField(upload_to='Course_Languages_video/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    course = models.ForeignKey(Course, related_name='course_languages', on_delete=models.CASCADE)

    def __str__(self):
        return self.language

    class Meta:
        indexes = [
            models.Index(fields=['language']),
        ]


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True, null=True)
    video_file = models.FileField(blank=True, null=True)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AssignmentSubmission(models.Model):
    students = models.ManyToManyField(UserProfile, related_name='submissions')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    submission_file = models.FileField(upload_to='submissions/', blank=True, null=True)
    grade = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 101)], null=True, blank=True,
                                             verbose_name='Оценка на задачи')

    submitted_at = models.DateTimeField(auto_now_add=True)


class Exam(models.Model):
    title_exam = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    passing_score = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 101)], null=True,
                                                     blank=True,
                                                     verbose_name='Оценка на экзамен')
    duration = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title_exam


class Question(models.Model):
    title_question = models.CharField(max_length=100)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='question')


    def __str__(self):
        return self.title_question

class Options(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    OPTION_CHOICES = (
        ('A', 'A'),
        ('Б', 'Б'),
        ('В', 'В'),
        ('Г', 'Г'),

    )
    options_choices = models.CharField(max_length=25, choices=OPTION_CHOICES)
    options_text = models.TextField()


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='certificate_student')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='certificate_course')
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField(null=True, blank=True)
    certificate_file = models.FileField(null=True, blank=True)


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True,
                                             verbose_name='Рейтинг')
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars} - {self.user.username}'


class Cart(models.Model):
    user = models.OneToOneField(Student, related_name='cart', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        total_price = sum(item.get_total_price() for item in self.items.all())
        return total_price


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.course.price * self.quantity

    def __str__(self):
        return f'{self.course} - {self.quantity}'


class Order(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='client')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('Оплачено', 'Оплачено'),
        ('Не Оплачено', 'Не Оплачено'),

    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='Ожидает оброботки')
    creates_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} - {self.status}'
