from rest_framework.test import APITestCase


class TestCases(APITestCase):
    def setUp(self):
        data = {"title": "TEST-CASE", "year": 1999, "rating": 1, "notes": "test"}
        self.client.post('/api/', data, format='json')

    def test_get_one(self):
        response = self.client.get('/api/1/')
        self.assertEqual(response.status_code, 200)

    def test_get_all(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post(self):
        data = {"title": "TEST-CASE", "year": 1999, "rating": 1, "notes": "test"}
        response = self.client.post('/api/', data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_post_invalid_rating_value(self):
        data = {"title": "TEST-CASE", "year": 1999, "rating": 11, "notes": "test"}
        response = self.client.post('/api/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_post_invalid_year_value(self):
        data = {"title": "TEST-CASE", "year": 9999, "rating": 10, "notes": "test"}
        response = self.client.post('/api/', data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_delete(self):
        response = self.client.delete('/api/1/')
        self.assertEqual(response.status_code, 204)

    def test_delete_non_existent(self):
        response = self.client.delete('/api/9999/')
        self.assertEqual(response.status_code, 404)

    def test_put(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 1999, "rating": 1, "notes": "test"}
        response = self.client.put('/api/1/', put_data, format='json')
        self.assertEqual(response.data['title'], "TEST-CASE-EDITED")

    def test_put_invalid_year(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 9999, "rating": 1, "notes": "test"}
        response = self.client.put('/api/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_put_invalid_rating(self):
        put_data = {"title": "TEST-CASE-EDITED", "year": 2000, "rating": 99, "notes": "test"}
        response = self.client.put('/api/1/', put_data, format='json')
        self.assertEqual(response.status_code, 400)