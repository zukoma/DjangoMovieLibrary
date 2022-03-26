from django_movie_library.movie.models import Movie
from django_movie_library.movie.tests import TestEnvSetUp


# class PostTests(TestEnvSetUp):
#     def test_get_recommendation(self):
#         data = {"genre": "Drama"}
#         response = self.client.post('/recommend/', data, format='json')
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(len(Movie.objects.all()), 1)