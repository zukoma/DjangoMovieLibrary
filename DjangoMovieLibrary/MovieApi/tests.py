from rest_framework.test import APITestCase
from DjangoMovieLibrary.MovieApi.models import Genre, Movie
from django.contrib.auth.models import User


class TestEnvSetUp(APITestCase):
    def setUp(self):
        test_genre = Genre(name="Drama")
        test_genre.save()

        test_user = User(username="test")
        test_user.save()

        test_movie = Movie(title="Test-Movie", year=1994, rating=10, notes="Test-notes", added_by=test_user)
        test_movie.save()


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

    def test_genre_get_one(self):
        response = self.client.get('/api/genres/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,  {'id': 1, 'name': 'Drama'})

    def test_genre_get_all(self):
        response = self.client.get('/api/genres/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class PostTests(TestEnvSetUp):
    def test_movie_post(self):
        data = {"title": "POST-TEST-CASE", "year": 1999, "rating": 1, "notes": "test", "genre": [1], "added_by": 1}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movie.objects.get(pk=2).title, "POST-TEST-CASE")
        self.assertEqual(Movie.objects.get(pk=2).year, 1999)
        self.assertEqual(Movie.objects.get(pk=2).rating, 1)
        self.assertEqual(Movie.objects.get(pk=2).notes, "test")

    def test_movie_post_invalid_rating_value(self):
        data = {"title": "TEST-CASE", "year": 1999, "rating": 11, "notes": "test"}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(Movie.objects.all()), 1)

    def test_movie_post_invalid_year_value(self):
        data = {"title": "TEST-CASE", "year": 9999, "rating": 10, "notes": "test"}
        response = self.client.post('/api/movies/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(Movie.objects.all()), 1)

    def test_genre_post(self):
        data = {'name': 'Thriller'}
        response = self.client.post('/api/genres/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Genre.objects.get(pk=2).name, "Thriller")


class DeleteTests(TestEnvSetUp):
    def test_movie_delete(self):
        response = self.client.delete('/api/movies/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Movie.objects.all()), 0)

    def test_movie_delete_non_existent(self):
        response = self.client.delete('/api/movies/9999/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(len(Movie.objects.all()), 1)

    def test_genre_delete(self):
        response = self.client.delete('/api/genres/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Genre.objects.all()), 0)


class PutTests(TestEnvSetUp):
    def test_movie_put(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 1999, "rating": 1, "notes": "test", "genre": [1], "added_by": 1}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.data['title'], "TEST-CASE-EDITED")
        self.assertEqual(Movie.objects.get(pk=1).title, "TEST-CASE-EDITED")

    def test_movie_put_invalid_year(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 9999, "rating": 1, "notes": "test", "genre": [1], "added_by": 1}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Movie.objects.get(pk=1).year, 1994)

    def test_put_invalid_rating(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 2000, "rating": 99, "notes": "test", "genre": [1], "added_by": 1}
        response = self.client.put('/api/movies/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Movie.objects.get(pk=1).rating, 10)

    def test_genre_put(self):
        data = {'name': 'Comedy'}
        response = self.client.put('/api/genres/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Genre.objects.get(pk=1).name, "Comedy")