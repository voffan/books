from django.contrib import admin
from bookshop.models import Author, Book
# Register your models here.


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_filter = ['full_name']
    search_fields = ['full_name']


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    #list_display = ['name', 'date', 'authors']
    search_fields = ['name', 'authors']
    list_filter = ['name', 'authors']


