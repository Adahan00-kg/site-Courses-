from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin



class SkillsInline(TranslationInlineModelAdmin,admin.TabularInline):
    model = Skills
    extra = 1


class CourseLanguagesInline(TranslationInlineModelAdmin,admin.TabularInline):
    model = CourseLanguages
    extra = 1

class LessonInline(TranslationInlineModelAdmin,admin.TabularInline):
    model = Lesson
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class ExamAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]



@admin.register(Course)
class CoursesAdmin(TranslationAdmin):
    inlines = [LessonInline,CourseLanguagesInline,SkillsInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Category,Assignment)
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
admin.site.register(Exam, ExamAdmin)
admin.site.register(Certificate)
admin.site.register(Review)








