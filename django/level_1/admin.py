from django.contrib import admin

from .models import Quiz, Question, Emotion, Person

class QuizInline(admin.TabularInline):
    model = Quiz
    max_num = 1

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    inlines = [
        QuizInline,
    ]


class EmotionInline(admin.TabularInline):
    model = Emotion
    extra = 4
    max_num = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        EmotionInline,
    ]

admin.site.register(Emotion)