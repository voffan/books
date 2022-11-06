from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.urls import reverse
from bookshop.models import Book, Author
from bookshop.serializers import BookSerializer, AuthorSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# Create your views here.


class BookRestView(APIView):
    def get_object(self, id):
        return get_object_or_404(Book, pk=id)

    def get(self, request, id, format=None):
        book = self.get_object(id)
        ser = BookSerializer(book)
        return Response(ser.data)

    def post(self, request, id, format=None):
        book = self.get_object(id)
        result = {'result': False, 'message': ''}
        if request.method == 'POST':
            ser = BookSerializer(book, request.data)
            if ser.is_valid():
                ser.save()
                result['result'] = True
                result['book'] = ser.data
            else:
                result['message'] = str(ser.error_messages)
        return Response(result)

    def delete(self, request, id, format=None):
        result = {'result': True, 'message': ''}
        if request.method == 'DELETE':
            book = self.get_object(id)
            try:
                result['book'] = book.id
                book.delete()
            except:
                del result['book']
                result['result'] = False
                result['message'] = 'Ошибка при удалении книги!'
        return Response(result)


class AddBookRestView(APIView):

    def post(self, request, format=None):
        result = {'result': False, 'message': ''}
        if request.method == 'POST':
            print(request.data)
            ser = BookSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                result['result'] = True
                result['book'] = ser.data
                result['book']['url'] = reverse('api:bookdetail', kwargs={'id':ser.data['id']})
            else:
                result['message'] = str(ser.error_messages)
        return Response(result)


class AuthorListRestView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
