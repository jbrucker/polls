from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    """customize appearance of Question in admin console"""
    fields = ["pub_date", "question_text"]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
