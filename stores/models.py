from django.db import models

class Store(models.Model):

    store_name = models.CharField("store_name", max_length=254)


class Product(models.Model):

    title = models.CharField("title", max_length=254)
    link = models.URLField("link")
    description = models.TextField("description")
    image_link = models.URLField("image_link")
    
