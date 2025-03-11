from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Lang (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL, null=True)
    summary = models.TextField()
    isbin = models.CharField('ISBiN',max_length=50,unique=True)
    genre = models.ManyToManyField(Genre)
    lang = models.ForeignKey(Lang, on_delete=models.SET_NULL, null=True)
    img = models.ImageField(upload_to='books/')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("BookDetail", kwargs={"pk": self.pk})
    


class Author (models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    BirthDate = models.DateField(blank=True , null=True)


    class Meta:
        ordering = ['FirstName' , 'LastName']

    def get_absolute_url(self):
        return reverse("AuthorDetail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return f'{self.LastName} - {self.FirstName}'
    

import uuid


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    inprint = models.CharField(max_length=1000)
    due_back = models.DateField(null=True,  blank=True)

    loan_status = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=20,choices= loan_status , default='m')

    class Meta:
        ordering = ['due_back']


    def __str__(self):
        return f'{self.id} ({self.book.title})'
