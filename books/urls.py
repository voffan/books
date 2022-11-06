"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookshop.views import BookListView, BookRestView, AuthorListRestView, AddBookRestView

api = [
    path('book/<int:id>', BookRestView.as_view(), name='bookdetail'),
    path('addbook', AddBookRestView.as_view(), name='addbook'),
    path('authors', AuthorListRestView.as_view({'get': 'list'}), name='authorlist')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='index'),
    path('api/', include((api, 'bookshop'), namespace='api')),
]
