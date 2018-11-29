from django.test import TestCase
from django.utils import timezone

from polls.models import Question, Choice

# Create your tests here.

class QuestionModelsTests(TestCase):
    def test_create_question(self):
        q = Question(question_text="This is a test")
        self.assertEqual(q.question_text, "This is a test")

    def test_create_choice(self):
        q = Question(question_text="What day is it?",pub_date=timezone.now())
        q.save()
        c1 = Choice(choice_text="Monday",question=q)
        c2 = Choice(choice_text="Tuesday",question=q)
        c3 = Choice(choice_text="Sunday",question=q)
        c1.save()
        c2.save()
        c3.save()
        self.assertEqual(3, len(q.choice_set.all()) )

