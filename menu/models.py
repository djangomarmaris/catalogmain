from django.db import models
from django.urls import reverse
# Create your models here.
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, db_index=True, unique=True)
    image = models.ImageField(upload_to='products/%y/%m/%d')
    info = models.CharField(max_length=58, db_index=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Category', on_delete = models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    info = RichTextUploadingField()
    full_info = RichTextUploadingField()
    price = models.DecimalField(max_digits=10, decimal_places=0)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name




    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id,self.slug])



class Sale(models.Model):
    discount = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True,verbose_name='570x301')
    link = models.CharField(max_length=200, db_index=True)



    def __str__(self):
        return self.name


class Shot(models.Model):
    discount = models.CharField(max_length=200, db_index=True)
    name = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%y/%m/%d', blank=True, verbose_name='652x471')
    link = models.CharField(max_length=200, db_index=True)


    def __str__(self):
        return self.name



class Restaurant(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    link = models.CharField(max_length=200, db_index=True)
    facebook = models.CharField(max_length=200, db_index=True)
    instagram = models.CharField(max_length=200, db_index=True)
    twitter = models.CharField(max_length=200, db_index=True)
    location = models.CharField(max_length=200, db_index=True)
    map = models.CharField(max_length=200, db_index=True)
    day = models.CharField(max_length=200, db_index=True)
    dayend = models.CharField(max_length=200, db_index=True)
    phone = models.CharField(max_length=200, db_index=True)

    class Meta:
        verbose_name = 'İnformations'

    def __str__(self):
        return self.name



