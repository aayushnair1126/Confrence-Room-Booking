from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)


class Detials(models.Model):
    authorname = models.CharField(max_length=100)
    book_price = models.CharField(max_length=3)
    genre= models.CharField(max_length=15)
    title= models.ForeignKey(Book,on_delete=models.CASCADE)
    
