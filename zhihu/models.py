from django.db import models

# Create your models here.

#创建用户信息表
class User(models.Model):
    class Meta:
        db_table = 'UserInfo'
    id = models.AutoField(primary_key=True, max_length=500, db_column='UID')
    UserName = models.CharField(max_length=50, db_column='username', blank=False)
    Password = models.CharField(max_length=50, db_column='password', blank=False)
    Phone = models.CharField(max_length=15, db_column='phone', blank=False)

#从数据库中读取知乎问题
class Questions(models.Model):
    class Meta:
        db_table = 'Questions'
    questionId = models.AutoField(primary_key=True, max_length=1000,db_column='QuestionID')
    Question = models.CharField(max_length=1000, db_column='question', blank=True)

#由对应问题ID作为外键从而获取对应的答案
class Answers(models.Model):
    class Meta:
        db_table = 'Answers'
    id = models.AutoField(primary_key=True, max_length=1000,db_column='AnswerID')
    question = models.ForeignKey(Questions, null=True, blank=True)
    Answer = models.CharField(max_length=1000, db_column='answer', blank=True)


