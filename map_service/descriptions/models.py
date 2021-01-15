from django.db import models
from django.urls import reverse


# class Article(models.Model):
#     title = models.CharField(max_length=100)
#     abstract = models.CharField(max_length=510)
#     content = models.TextField()
#     artic_date = models.DateTimeField(default=timezone.now)
#     img = models.FileField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('article-detail', kwargs={'pk': self.pk})


# class Image(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     author = models.CharField(max_length=100)
#     desc = models.CharField(max_length=100, default='description')
#     file = models.FileField()

#     def __str__(self):
#         return self.name
