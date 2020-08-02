from django.db import models

# Create your models here.
class Candidate(models.Model):
    name = models.CharField(max_length=10) #이름
    job = models.CharField(max_length=10) #직업 시민
    votes = models.IntegerField(default=0)#득표수 0
    life = models.BooleanField(default=True)#True
    img = models.ImageField(blank=True)#파일업로드

    # 받지 않았다면 0으로 하기 위해

    def __str__(self):
        return self.name
