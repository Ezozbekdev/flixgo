from django.test import TestCase
from .models import Movie


class PostMovie(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Movie.objects.create(
            title='Spider man',
            img='spider.jpg',
            hd='HD',
            age_limit='+16',
            year='2022-02-01',
            time_run='60',
            country='USA',
            dic='Text',
            movie_hd='video.mp4',
            movie_720='video.mp4',
            movie_1440='video.mp4',
        )
