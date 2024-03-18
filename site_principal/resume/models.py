from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


class Resume(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    about = models.TextField('Sobre', max_length=900)    


class MainStack(models.Model):
    resume = models.ManyToManyField(Resume)
    name = models.CharField('Stack', max_length=90)
    description = models.TextField('Descrição', max_length=500)
    level = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = "Main Stack"
        verbose_name_plural = "Main Stacks"
    

class SubStack(models.Model):
    stack = models.ForeignKey(MainStack, verbose_name='Main stack', on_delete=models.CASCADE)
    name = models.CharField('Stack', max_length=90)
    description = models.TextField('Descrição', max_length=500)
    level = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = "Sub Stack"
        verbose_name_plural = "Sub Stacks"
