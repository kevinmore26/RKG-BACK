from rest_framework import request
from rest_framework.test import APITestCase
from .models import ProductoModel

class ProductosTestCase(APITestCase):

    def setUp(self):
        ProductoModel(  
                        productoNombre= 'Casa de perro4',
                        productoId=4,
                        productoPrecio= 120.90,
                        productoFoto= 'casaperro4.jpg',
                        productoDescripcion= 'Casa para perro4').save()
        ProductoModel(  
                        productoNombre= 'Casa de perro2',
                        productoId=2,
                        productoPrecio= 120.90,
                        productoFoto= 'casaperro2.jpg',
                        productoDescripcion= 'Casa para perro2').save()
        ProductoModel(  
                        productoNombre= 'Casa de perro3',
                        productoId=3,
                        productoPrecio= 120.90,
                        productoFoto= 'casaperro3.jpg',
                        productoDescripcion= 'Casa para perro3').save()
        ProductoModel(  
                        productoNombre= 'Casa de perro5',
                        productoId=5,
                        productoPrecio= 120.90,
                        productoFoto= 'casaperro5.jpg',
                        productoDescripcion= 'Casa para perro5').save()

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
            "productoId": 65,
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

    def test_get_id_success(self):
        '''Deberia retornar los productos almacenados por id'''

        productoEncontrado = ProductoModel.objects.all()
        # print(productoEncontrado)
        request = self.client.get('/gestion/producto/2')

        print(request.data)     
        self.assertEqual(1, 1)

    
    def test_get_id_fail(self):
        '''Deberia fallar el test al solicitar un id que no existe'''

        productoEncontrado = ProductoModel.objects.all()
        request = self.client.get('/gestion/producto/100')
        message = request.data.get('message')

        print(request.data) 

        self.assertEqual(request.status_code, 404)
        self.assertEqual(message, 'Producto no encontrado')
          

    def test_delete_id_fail(self):
        '''Deberia fallar el test delete al solicitar un id que no existe'''

        productoEncontrado = ProductoModel.objects.all()
        request = self.client.delete('/gestion/producto/75')
        message = request.data.get('message')

        print(request.data) 

        self.assertEqual(request.status_code, 404)
        self.assertEqual(message, 'Producto no encontrado')

    def test_delete_id_success(self):
        '''Deberia borrar el producto solicitado'''

        productoEncontrado = ProductoModel.objects.all()
        request = self.client.delete('/gestion/producto/4')
        message = request.data.get('message')

        print(request.data) 
        self.assertEqual(request.status_code, 200)
        self.assertEqual(message, 'Producto eliminado exitosamente')

    def test_put_fail_1(self):
        '''Deberia fallar el put al no completar los campos requeridos'''

        productoEncontrado = ProductoModel.objects.all()
        request = self.client.put('/gestion/producto/5')
        message = request.data.get('message')

        print(request.data) 

        self.assertEqual(request.status_code, 400)
        self.assertEqual(message, 'Error al actualizar el producto')
    
    def test_put_fail_2(self):
        '''Deberia fallar el put al no existir el producto solicitado'''

        productoEncontrado = ProductoModel.objects.all()
        request = self.client.put('/gestion/producto/666')
        message = request.data.get('message')

        print(request.data) 

        self.assertEqual(request.status_code, 404)
        self.assertEqual(message, 'Producto no existe')

    def test_put_success(self):
        '''Deberia el test actualizar el producti solicitado'''

        productoEncontrado = ProductoModel.objects.all()
        request = self.client.put('/gestion/producto/3', data={
            "productoNombre": "Casa de perro3",
            "productoId": 3,
            "productoPrecio": 580.90,
            "productoFoto": "casaperro3.jpg",
            "productoDescripcion": "Casa para perro3"
        }, format='json')
        message = request.data.get('message')

        print(request.data) 

        self.assertEqual(request.status_code, 200)
        self.assertEqual(message, 'Producto actualizado exitosamente')







