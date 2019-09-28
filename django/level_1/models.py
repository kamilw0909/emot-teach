from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=60)
    age = models.PositiveIntegerField()

class Quiz(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    score = models.PositiveIntegerField(default=1)


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Emotion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    img_url = models.ImageField()
    true_false_answer = models.BooleanField(max_length=10)

    def __str__(self):
        return self.name

