from django.shortcuts import render, redirect
from .forms import Book_form
from .models import *

# Create your views here.


def book_list(request):
    context = {'book_list': Detials.objects.all()}
    return render(request, "book_entry/book_list.html", context)


def book_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = Book_form()
        else:
            book = Detials.objects.get(pk=id)
            form = Book_form(instance=book)
        return render(request, "book_entry/book_form.html", {'form': form})
    else:
        if id == 0:
            form = Book_form(request.POST)
        else:
            book = Detials.objects.get(pk=id)
            form = Book_form(request.POST,instance= book)
        if form.is_valid():
            form.save()
        return redirect('/list')


def book_delete(request,id):
    book = Detials.objects.get(pk=id)
    book.delete()
    return redirect('/list')
