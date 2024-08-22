from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from movies.models import Actor, Movie


class MovieViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.movie1 = Movie.objects.create(name='Movie 1', genre='Action', imdb=7.5)
        self.movie2 = Movie.objects.create(name='Movie 2', genre='Drama', imdb=8.2)
        self.movie3 = Movie.objects.create(name='Movie 3', genre='Comedy', imdb=6.3)

    def test_list_movies(self):
        response = self.client.get('/path/to/your/movies/endpoint/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['name'], 'Movie 1')
        self.assertEqual(response.data[1]['name'], 'Movie 2')
        self.assertEqual(response.data[2]['name'], 'Movie 3')


# class TestGetCastedActors(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.actor = Actor.objects.create(name='Jamshid')
#         self.movie = Movie.objects.create(title='Jamshid')
#         self.movie.casted_actors.add(self.actor)

#     def test_get_casted_actors(self):
#         url = reverse('movie-detail', args=[self.movie.id])  # Use the correct URL name here
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('casted_actors', response.data)
#         self.assertEqual(response.data['casted_actors'][0]['name'], 'Jamshid')


# class TestMovieViewSet(TestCase):
#     def setUp(self) -> None:
#         self.movie = Movie.objects.create(name='Inception adda')
#         self.client = APIClient()
#
#
#     def test_order_by_imdb(self):
#         url = reverse('movie-list')
#         response = self.client.get(url, {'ordering': 'imdb'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 0)
#         self.assertEqual(response.data[6]['name'], 'The Matrix')
        # self.assertEqual(response.data[1]['name'], 'Inception')
        # self.assertEqual(response.data[2]['name'], 'The Godfather')