from django.db import models
from django.contrib.auth.models import User;

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,  related_name = "author_question");
    subject = models.CharField(max_length=200);
    content = models.TextField();
    create_date = models.DateTimeField();
    modify_date = models.DateTimeField(null = True, blank = True);
    voter = models.ManyToManyField(User, related_name = "voter_question");
    def __str__(self):
        return self.subject;

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'author_answer');
    question = models.ForeignKey(Question, on_delete=models.CASCADE);
    # 어떤 모델이 다른 모델을 속성으로 가지면 ForeignKey를 이용, 다른 모델과의 연결을 의미
    # on_delete = models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField();
    modify_date = models.DateTimeField(null=True, blank=True);
    voter = models.ManyToManyField(User, related_name="voter_answer");


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE);
    content = models.TextField();
    create_date = models.DateTimeField();
    modify_date = models.DateTimeField(null = True, blank = True);
    question = models.ForeignKey(Question, null = True, blank = True, on_delete=models.CASCADE);
    answer = models.ForeignKey(Answer, null = True, blank = True, on_delete=models.CASCADE);