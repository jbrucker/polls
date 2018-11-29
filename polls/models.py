from django.db import models
from django.utils import timezone

# Create your models here./hom/

class Question(models.Model):
    question_text = models.CharField('question',max_length=100)
    pub_date = models.DateTimeField('date published')

    @classmethod
    def create(cls, question, date=timezone.now()):
        """Create a new question.

        Usage: Question.create("question text"[,date_time])
        """
        return cls(question_text=question, pub_date=date)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

