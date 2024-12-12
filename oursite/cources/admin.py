from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class CourseLanguagesInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = CourseLanguages
    extra = 1


class LessonInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = Lesson
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


@admin.register(Course)
class CoursesAdmin(TranslationAdmin):
    inlines = [LessonInline, CourseLanguagesInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category, Assignment, Skills)
class ProductAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(AssignmentSubmission)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Certificate)
admin.site.register(Review)
admin.site.register(Exam)
admin.site.register(Country)
