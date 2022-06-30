from django.db import models


class Movie(models.Model):
    hd = 'HD'
    ty = (
        (hd, 'HD'),
    )
    title = models.CharField(max_length=250, blank=True, null=True)
    img = models.ImageField(upload_to='vmovi-img/')
    hd = models.CharField(max_length=120, choices=ty)
    age_limit = models.CharField(max_length=120)
    year = models.DateField()
    time_run = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    dic = models.TextField()
    movie_hd = models.FileField(upload_to='video/', blank=True, null=True)
    movie_720 = models.FileField(upload_to='video/', blank=True, null=True)
    movie_1440 = models.FileField(upload_to='video/', blank=True, null=True)

    def __str__(self):
        return self.title


class Faq(models.Model):
    question = models.CharField(max_length=210)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Share(models.Model):
    facebook = models.URLField()
    insta = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return f'{self.facebook} {self.insta} {self.twitter}'
