from django_movie_library.movie.models import Ratings
from django_movie_library.movie.tests import TestEnvSetUp


class GetTests(TestEnvSetUp):
    def test_ratings_get_one(self):
        response = self.client.get('/api/ratings/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,  {'user': 1, 'movie': 1, 'rating': 10})

    def test_ratings_get_all(self):
        response = self.client.get('/api/ratings/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


class PostTests(TestEnvSetUp):
    def test_ratings_post(self):
        data = {'user': 2, 'movie': 1, 'rating': 1}
        response = self.client.post('/api/ratings/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Ratings.objects.get(pk=2).rating, 1)


class DeleteTests(TestEnvSetUp):
    def test_ratings_delete(self):
        response = self.client.delete('/api/ratings/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Ratings.objects.all()), 1)


class PutTests(TestEnvSetUp):
    def test_ratings_put(self):
        data = {'user': 2, 'movie': 1, 'rating': 5}
        response = self.client.put('/api/ratings/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Ratings.objects.get(pk=1).rating, 5)
