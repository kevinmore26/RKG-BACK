from rest_framework.test import APITestCase
from .models import AdopcionModel





# ------------------------------------
class AdopcionesTestCase(APITestCase):

    def setUp(self):
        AdopcionModel(adopcionNombre='Adopcion1',
                      adopcionEdad="2", adopcionTamanio='P').save()    

    def test_post_fail(self):
        '''Deberia fallar el test si no pusiste nada'''
        
        request = self.client.post('/gestion/adopciones/')
        message = request.data.get("message")
        print(message)
        self.assertEqual(request.status_code, 400)
        self.assertEqual(message, 'Error al guardar la adopcion')

    def test_post_success(self):
        '''Deberia retornar el producto creado'''

        request = self.client.post('/gestion/adopciones/', data={
            "adopcionNombre": "LALA",
            "adopcionEdad": "3",
            "adopcionTamanio": "P",
            "adopcionFoto":"foto.jpg",
            "adopcionCaracteristicas":"Muy bonito"
        }, format='json')

        
        message = request.data.get('message')
        id = request.data.get('content').get('adopcionId')

        AdopcionEncontrada = AdopcionModel.objects.filter(adopcionId=id).first()
        print(request.data)

        self.assertEqual(request.status_code, 201)
        
       
        self.assertEqual(message, 'Adopcion creada exitosamente')
        self.assertIsNotNone(AdopcionEncontrada)

class BuscadoraAdopcionTestCase(APITestCase):
            
    def test_get_success(self):
        '''Deberia retornar las adopciones '''
        
        request = self.client.post('/gestion/adopciones/', data={
            "adopcionNombre": "tomy",
            "adopcionEdad": 3, 
            "adopcionTamanio": "P",
            
            "adopcionFoto":"foto.jpg",
            "adopcionCaracteristicas":"Muy bonito"
            
        }, format='json')
        message = request.data.get('message')
        
        id = request.data.get('content').get('adopcionId')
        adopcionEncontrada = AdopcionModel.objects.filter(
                adopcionId=id).first()
        
        self.assertEqual(request.status_code, 201)
        self.assertEqual(message, 'Adopcion creada exitosamente')
        self.assertIsNotNone(adopcionEncontrada)
    
    def test_get_fail(self):
        '''Debería no retornar los clientes'''
        request = self.client.get('/gestion/adopciones/')
        message = request.data.get('message')
        print(request.data)
        
        content = request.data.get('data').get('content')
        id = request.data.get('content').get('adopcionId')
        
        self.assertIsNone(content.data.get(id))
        self.assertEqual(request.status_code, 400)
        self.assertEqual(message, 'Adopcion no encontrada')