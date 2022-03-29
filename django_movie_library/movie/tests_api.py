from rest_framework.test import APITestCase
from django_movie_library.movie.models import Genre, Movie, Ratings
from django.contrib.auth.models import User


class TestEnvSetUp(APITestCase):
    def setUp(self):
        Genre.objects.create(name="Drama")

        user = User.objects.create(username="test")
        user2 = User.objects.create(username="test2")

        movie = Movie.objects.create(title="Test-Movie", year=1994, notes="Test-notes")
        movie2 = Movie.objects.create(title="Test-Movie2", year=2000, notes="Test-notes2")

        Ratings.objects.create(movie=movie, user=user, rating=10)
        Ratings.objects.create(movie=movie2, user=user2, rating=1)


class GetTests(TestEnvSetUp):
    def test_movie_get_one(self):
        response = self.client.get('/api/movies/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Test-Movie")
        self.assertEqual(response.data['year'], 1994)

    def test_movie_get_all(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


class PostTests(TestEnvSetUp):
    def test_movie_post(self):
        data = {"title": "POST-TEST-CASE", "year": 1999, "notes": "test", "genre": [1]}
        response = self.client.post('/api/movies/', data, format='json')
        posted_object = Movie.objects.get(pk=3)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(posted_object.title, "POST-TEST-CASE")
        self.assertEqual(posted_object.year, 1999)
        self.assertEqual(posted_object.notes, "test")

    def test_movie_post_invalid_genre_value(self):
        data = {"title": "TEST-CASE", "year": 1999, "notes": "test", "genre": [2]}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Movie.objects.count(), 2)

    def test_movie_post_invalid_year_value(self):
        data = {"title": "TEST-CASE", "year": 9999, "rating": 10, "notes": "test"}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Movie.objects.count(), 2)


class DeleteTests(TestEnvSetUp):
    def test_movie_delete(self):
        response = self.client.delete('/api/movies/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Movie.objects.count(), 1)

    def test_movie_delete_non_existent(self):
        response = self.client.delete('/api/movies/9999/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Movie.objects.count(), 2)


class PutTests(TestEnvSetUp):
    def test_movie_put(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 1999, "notes": "test", "genre": [1]}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.data['title'], "TEST-CASE-EDITED")
        self.assertEqual(Movie.objects.get(title="TEST-CASE-EDITED").title, "TEST-CASE-EDITED")

    def test_movie_put_invalid_year(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 9999, "notes": "test", "genre": [1]}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Movie.objects.get(year=1994).year, 1994)

    def test_put_invalid_genre(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 2000, "notes": "test", "genre": [3]}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)