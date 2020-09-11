from django.db import models
class Question (models.Model):
   qtext=models.CharField(max_length=200)
   qdate=models.DateTimeField('date published')
   def __str__(self):
       return self.qtext

class Choice (models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    ctext=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
       return self.ctext

