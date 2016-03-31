from django.shortcuts import render
from django.http import HttpResponse


'''def index (request):
    return HttpResponse ("Hello Mark, You're in newBook index.")
'''

def get_new_book (request):
    return render (request, 'newbook/new_book.html', {})