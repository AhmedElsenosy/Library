from django.shortcuts import render , HttpResponse
from . import models
from django.views import generic

# Create your views here.
def index(request):
    BooksNum = models.Book.objects.all().count()
    BooksNumInstance = models.BookInstance.objects.all().count()
    BooksNumAvailable = models.BookInstance.objects.filter(status__exact='a').count()

    context = {
        'BooksNum': BooksNum,
        'BooksNumInstance': BooksNumInstance,
        'BooksNumAvailable': BooksNumAvailable,
    }
    return render(request,'index.html',context)


class BookCreate(generic.CreateView):
    model = models.Book
    fields = '__all__'
    success_url = '/cataloge'
    template_name = 'create.html'

class BookDetail(generic.DetailView):
    model = models.Book
    template_name = 'detail.html'
    context_object_name = 'book'