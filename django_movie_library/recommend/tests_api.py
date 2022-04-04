from django_movie_library.recommend.models import Recommendations
from django_movie_library.movie.tests_api import TestEnvSetUp


class GetTests(TestEnvSetUp):
    def test_get_recommendations(self):
        response = self.client.get('/api/recommendations/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Recommendations.objects.count(), 1)

    def test_get_one_recommendation(self):
        response = self.client.get('/api/recommendations/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['id'], 1)

    def test_get_invalid_recommendation(self):
        response = self.client.get('/api/recommendations/999/')
        self.assertEqual(response.status_code, 404)


class PostTests(TestEnvSetUp):
    def test_get_recommendation(self):
        data = {"genre": "Drama",
                "user": "test"}

        response = self.client.post('/recommend/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Recommendations.objects.count(), 2)

    def test_post_invalid_recommendation(self):
        data = {"genre": "Horror",
                "user": "human"}

        response = self.client.post('/recommend/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Recommendations.objects.count(), 1)


class DeleteTests(TestEnvSetUp):
    def test_delete_recommendation(self):
        response = self.client.delete('/api/recommendations/1/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Recommendations.objects.count(), 0)

    def test_delete_invalid_recommendation(self):
        response = self.client.delete('/api/recommendations/1999/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Recommendations.objects.count(), 1)
