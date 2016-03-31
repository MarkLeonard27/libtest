from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import BookDetails


'''def index (request):
    return HttpResponse ("Hello Mark, You're in newBook index.")
'''

def get_new_book (request):
    books = BookDetails.objects.all()
    return render (request, 'newbook/new_book.html', {'books': books})