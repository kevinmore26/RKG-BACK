from rest_framework.test import APITestCase

class ProductosTestCase(APITestCase):
    def test_post(self):
        request = self.client.post('/gestion/productos/')
        print(request.status_code)
        print(request.data)

        self.assertEqual(1, 1)