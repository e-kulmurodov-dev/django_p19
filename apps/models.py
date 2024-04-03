from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django_ckeditor_5.fields import CKEditor5Field


class ContactModel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='contacts/')

    def __str__(self):
        return self.name

















#
# # Create your models here.
# #
# # class Category(models.Model):
# #     name = models.CharField(max_length=255)
# #
# #     def __str__(self):
# #         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.FloatField()
#     description = CKEditor5Field(config_name='extends')
#     category = models.ForeignKey('apps.Category', CASCADE)
#
#     def __str__(self):
#         return self.name
#
#
# class Region(models.Model):
#     name = models.CharField(max_length=255)
#
#
# class District(models.Model):
#     name = models.CharField(max_length=255)
#     region = models.ForeignKey('apps.Region', CASCADE)
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     last_update = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class FilmCategory(models.Model):
#     film = models.ForeignKey('apps.Film', CASCADE)
#     category = models.ForeignKey('apps.Category', CASCADE)
#     last_update = models.CharField(max_length=255)
#
#     # ASK QUESTION
#     def __str__(self):
#         return self.film_id
#
#
# class Film(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     release_year = models.CharField(max_length=255)
#     language = models.ForeignKey('apps.Language', CASCADE)
#     rental_duration = models.IntegerField(default=3)
#     rental_rate = models.FloatField(default=4.99)
#     length = models.IntegerField()
#     replacement_cost = models.FloatField(default=19.99)
#     rating = models.CharField(max_length=255)
#     last_update = models.CharField(max_length=255)
#     special_features = models.TextField()
#     fulltext = models.TextField()
#
#
# class Language(models.Model):
#     name = models.CharField(max_length=255)
#     last_update = models.CharField(max_length=255)
#
#
# #
# # class FilmImages(models.Model):
# #     image = models.ImageField(upload_to='film/')
# #     film = models.ForeignKey('apps.Film', CASCADE)
# #
#
# # class BaseModel(models.Model):
# #     created_at = models.DateTimeField(auto_now_add=True)
# #
# #     class Meta:
# #         abstract = True
# #
# #
# # class NewProduct(BaseModel):
# #     name = models.CharField(max_length=255)
#
#
# class Post(models.Model):
#     user = models.ForeignKey('auth.User', CASCADE)
#     title = models.CharField(max_length=255)
#     body = models.TextField()
#
#     def __str__(self):
#         return self.title
#
#
# class Comment(models.Model):
#     post = models.ForeignKey('apps.Post', CASCADE)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     body = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class Album(models.Model):
#     user = models.ForeignKey('auth.User', CASCADE)
#     title = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title
#
#
# class Photo(models.Model):
#     album = models.ForeignKey('apps.Album', CASCADE)
#     title = models.CharField(max_length=255)
#     url = models.URLField()
#     thumbnail_url = models.URLField()
#
#     def __str__(self):
#         return self.title
#
#
# class Todo(models.Model):
#     user = models.ForeignKey('auth.User', CASCADE)
#     title = models.CharField(max_length=255)
#     completed = models.BooleanField()
#
#     def __str__(self):
#         return self.title
#
