from django.db import models
from django.contrib.auth.models import User

class SocialMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    linkedin = models.CharField('LinkedIn', max_length=150, default=None)
    x = models.CharField('X', max_length=150, default=None)
    github = models.CharField('GitHub', max_length=150, default=None)
    kaggle = models.CharField('Kaggle', max_length=150, default=None)
    telegram = models.CharField('Telegram', max_length=150, default=None)

    def __str__(self) -> str:
        return self.user.username
    
    
class PersonalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birthday = models.DateField('Nascimento')
    about = models.TextField('Sobre', max_length=500)
    gender = models.CharField('Sexo', max_length=1, choices=[('M', 'M'),('F', 'F')])

    def __str__(self) -> str:
        return self.user.username
        