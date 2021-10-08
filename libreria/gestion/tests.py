from rest_framework.test import APITestCase
from .models import ProductoModel

class ProductosTestCase(APITestCase):

    def setUp(self):
        ProductoModel(  productoNombre= 'Casa de perro',
                        productoPrecio= 120.90,
                        productoFoto= 'casaperro.jpg',
                        productoDescripcion= 'Casa para perro').save()

    def test_post_fail(self):
        '''Deberia fallar el test cuando no le pasamos la informacion'''
        # print(self.shortDescription())

        request = self.client.post('/gestion/productos/')
        message = request.data.get('message')

        self.assertEqual(request.status_code, 400)
        self.assertEqual(message, 'Error al crear el producto')
    
    def test_post_success(self):
        '''Deberia retornar el producto creado'''
        # print(self.shortDescription())

        request = self.client.post('/gestion/productos/', data={
            "productoNombre": "Casa de perro",
            "productoPrecio": 120.90,
            "productoFoto": "casaperro.jpg",
            "productoDescripcion": "Casa para perro2"
        }, format='json')
        message = request.data.get('message')
        id = request.data.get('content').get('productoId')
        print(id)
        productoEncontrado = ProductoModel.objects.filter(
            productoId=id).first()

        self.assertEqual(request.status_code, 201)
        self.assertEqual(message, 'Producto creado exitosamente')
        self.assertIsNotNone(productoEncontrado)


    def test_get_success(self):
        '''Deberia retornar los productos almacenados'''

        productoEncontrado = ProductoModel.objects.all()
        print(productoEncontrado)

        self.assertEqual(1, 1)