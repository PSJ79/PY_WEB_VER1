from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True)
    description = models.CharField('Description', max_length=100, blank=True, help_text='simple description')
    create_date = models.DateTimeField('Create Date', auto_now=True, blank=True, help_text='create date')
    modify_date = models.DateTimeField('Modify Date', auto_now=True, blank=True, help_text='modify date')

    def __str__(self):
        return self.title
