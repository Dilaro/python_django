import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Текст вопроса")
    pub_date = models.DateTimeField(verbose_name="Дата публикации")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    def get_absolute_url(self):
        return reverse('polls:index')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    choice_text = models.CharField(max_length=200, verbose_name="Текст ответа")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def get_absolute_url(self):
        return reverse('polls:index')