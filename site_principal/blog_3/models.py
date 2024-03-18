from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from stdimage import StdImageField
from ..resume.models import Resume
#djangofrom django.core.validators import MaxValueValidator, MinValueValidator



class Base(models.Model):
    """
    Cria ums classe base para ser herdada para as demais com 
    campos genéricos.
    """
    created = models.DateTimeField('Data de criação', auto_now_add=True)
    modified = models.DateTimeField('Data de modificação', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Biscoito(Base):
    author = models.CharField(name='Autor', max_length=100)
    sentence = models.TextField(name='Frase', max_length=250)
    added_by = models.ForeignKey(get_user_model(), verbose_name='Adicionado por', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Biscoito'
        verbose_name_plural = 'Biscoitos'

    
    def __str__(self) -> str:
        return self.sentence


class Assuntos(Base):
    assunto = models.CharField(name='Assunto', max_length=100)
    added_by = models.ForeignKey(get_user_model(), verbose_name='Adicionado por', on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.assunto
    
    class Meta:
        verbose_name = 'Assunto'
        verbose_name_plural = 'Assuntos'


class Post(Base):
    title = models.CharField('Título', max_length=150)
    author = models.ForeignKey(get_user_model(), verbose_name='Escrito por', on_delete=models.CASCADE)
    likes = models.IntegerField('Curtidas', default=0)
    body = RichTextField(blank=True, null=True)
    subjects = models.ManyToManyField(Assuntos)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'


class Projeto(Base):
    title = models.CharField('Título', max_length=150)
    author = models.ForeignKey(get_user_model(), verbose_name='Escrito por', on_delete=models.CASCADE)
    picture = StdImageField()
    subjects = models.ManyToManyField(Assuntos)

    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

'''
class MainStack(Base):
    name = models.CharField('Stack', max_length=90)
    description = models.TextField('Descrição', max_length=500)
    domain = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = "Stack"
        verbose_name_plural = "Stacks"
    

class SubStack(Base):
    stack = models.ForeignKey(MainStack, verbose_name='Main stack', on_delete=models.CASCADE)
    name = models.CharField('Stack', max_length=90)
    description = models.TextField('Descrição', max_length=500)
    domain = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = "Stack"
        verbose_name_plural = "Stacks"
'''

class Comentarios(Base):
    pass