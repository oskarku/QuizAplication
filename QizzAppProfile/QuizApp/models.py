from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    content = models.TextField(verbose_name="Treść pytania")
    option_a = models.CharField(max_length=255, verbose_name="Opcja A")
    option_b = models.CharField(max_length=255, verbose_name="Opcja B")
    option_c = models.CharField(max_length=255, verbose_name="Opcja C")
    option_d = models.CharField(max_length=255, verbose_name="Opcja D")
    correct_answer = models.CharField(max_length=1, verbose_name="Poprawna odpowiedź")

    def __str__(self):
        return self.content

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quizzes_taken = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Quiz(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

    def __str__(self):
        return self.question_text


class QuizSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.quiz.name}'