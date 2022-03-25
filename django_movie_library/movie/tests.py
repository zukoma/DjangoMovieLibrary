from rest_framework.test import APITestCase
from django_movie_library.movie.models import Genre, Movie, Ratings
from django.contrib.auth.models import User


class TestEnvSetUp(APITestCase):
    def setUp(self):
        test_genre = Genre(name="Drama")
        test_genre.save()

        test_user = User(username="test")
        test_user.save()

        test_movie = Movie(title="Test-Movie", year=1994, notes="Test-notes")
        test_movie.save()

        test_rating = Ratings(movie=test_movie, user=test_user, rating=10)
        test_rating.save()


class GetTests(TestEnvSetUp):
    def test_movie_get_one(self):
        response = self.client.get('/api/movies/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Test-Movie")
        self.assertEqual(response.data['year'], 1994)

    def test_movie_get_all(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class PostTests(TestEnvSetUp):
    def test_movie_post(self):
        data = {"title": "POST-TEST-CASE", "year": 1999, "notes": "test", "genre": [1]}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.get(pk=2).title, "POST-TEST-CASE")
        self.assertEqual(Movie.objects.get(pk=2).year, 1999)
        self.assertEqual(Movie.objects.get(pk=2).notes, "test")

    def test_movie_post_invalid_genre_value(self):
        data = {"title": "TEST-CASE", "year": 1999, "notes": "test", "genre": [2]}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(Movie.objects.all()), 1)

    def test_movie_post_invalid_year_value(self):
        data = {"title": "TEST-CASE", "year": 9999, "rating": 10, "notes": "test"}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(Movie.objects.all()), 1)


class DeleteTests(TestEnvSetUp):
    def test_movie_delete(self):
        response = self.client.delete('/api/movies/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Movie.objects.all()), 0)

    def test_movie_delete_non_existent(self):
        response = self.client.delete('/api/movies/9999/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(Movie.objects.all()), 1)


class PutTests(TestEnvSetUp):
    def test_movie_put(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 1999, "notes": "test", "genre": [1]}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.data['title'], "TEST-CASE-EDITED")
        self.assertEqual(Movie.objects.get(pk=1).title, "TEST-CASE-EDITED")

    def test_movie_put_invalid_year(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 9999, "notes": "test", "genre": [1]}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Movie.objects.get(pk=1).year, 1994)

    def test_put_invalid_genre(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 2000, "notes": "test", "genre": [3]}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)