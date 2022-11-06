from django.db import models

# Create your models here.

class Author(models.Model):
    full_name = models.CharField('ФИО', max_length=200, db_index=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name


class Book(models.Model):
    name = models.CharField('Название', max_length=250, db_index=True)
    description = models.TextField('Описание')
    date = models.DateField('Дата добавления', auto_now_add=True, db_index=True)
    authors = models.ManyToManyField(Author, verbose_name='Авторы', db_index=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return ','.join([author.full_name for author in self.authors.all()]) + ' ' + self.name

    @property
    def short_description(self):
        return ' '.join(self.description.split()[:10]) + '...'
