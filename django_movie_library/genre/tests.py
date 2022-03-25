from django_movie_library.movie.models import Genre
from django_movie_library.movie.tests import TestEnvSetUp


class GetTests(TestEnvSetUp):
    def test_genre_get_one(self):
        response = self.client.get('/api/genres/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data,  {'id': 1, 'name': 'Drama'})

    def test_genre_get_all(self):
        response = self.client.get('/api/genres/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class PostTests(TestEnvSetUp):
    def test_genre_post(self):
        data = {'name': 'Thriller'}
        response = self.client.post('/api/genres/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Genre.objects.get(pk=2).name, "Thriller")


class DeleteTests(TestEnvSetUp):
    def test_genre_delete(self):
        response = self.client.delete('/api/genres/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Genre.objects.all()), 0)


class PutTests(TestEnvSetUp):
    def test_genre_put(self):
        data = {'name': 'Comedy'}
        response = self.client.put('/api/genres/1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Genre.objects.get(pk=1).name, "Comedy")