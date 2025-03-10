from django.shortcuts import render 
from . import models
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# @login_required
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


class BookCreate(LoginRequiredMixin,generic.CreateView):
    model = models.Book
    fields = '__all__'
    success_url = '/cataloge'
    template_name = 'create.html'

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'


class BookDetail(generic.DetailView):
    model = models.Book
    template_name = 'detail.html'
    context_object_name = 'book'