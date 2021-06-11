from django.contrib import admin
from .models import *

class cust(admin.ModelAdmin):

    list_display = ['title']

admin.site.register(Book,cust)

class Detail(admin.ModelAdmin):

    list_display = ['authorname','book_price','genre','title']

admin.site.register(Detials,Detail)
