from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BookForm
from .models import Book



# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')
    #return HttpResponse("Hello, this is the homepage!")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books' : books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form' : form})