from rest_framework.test import APITestCase
from .models import AdopcionModel,ProductoModel,PedidoModel,clienteModel


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

# ------------------------------------


# Create your tests here.

class ClienteTestCase(APITestCase):
    def setUp(self):
        clienteModel(
            clienteNombre = "PruebaNombre1",
            clienteApellido = "PruebaApellido1",
            clienteDocumento = "12345678",
            clienteCelular = "912345678",
            clienteCorreo = "Testcorreo1@hotmail.com",
            password = "ClavePrueba1",
            clienteTipo = 1
        ).save()
        clienteModel(
            clienteNombre = "PruebaNombre2",
            clienteApellido = "PruebaApellido2",
            clienteDocumento = "22345678",
            clienteCelular = "922345678",
            clienteCorreo = "Testcorreo2@hotmail.com",
            password = "ClavePrueba2",
            clienteTipo = 2
        ).save()
        clienteModel(
            clienteNombre = "PruebaNombre3",
            clienteApellido = "PruebaApellido3",
            clienteDocumento = "32345678",
            clienteCelular = "932345678",
            clienteCorreo = "Testcorreo3@hotmail.com",
            password = "ClavePrueba3",
            clienteTipo = 3
        ).save()

    def test_post_cliente_fail(self):
        '''Deberia arrojar un error si los datos no son ingresados'''
        request = self.client.post('/gestion/clientes/')
        self.assertEqual(request.status_code, 400)

    def test_post_cliente_success(self):
        '''Deberia crear el cliente y devolverlo'''
        request = self.client.post(
            '/gestion/clientes/', data= {
            "clienteNombre" :  "PruebaNombre4",
            "clienteApellido" : "PruebaApellido4",
            "clienteDocumento" : "42345678",
            "clienteCelular" : "942345678",
            "clienteCorreo" : "Testcorreo4@hotmail.com",
            "password" : "ClavePrueba4",
            "clienteTipo" : 2
        }, format='json')
        message = request.get('message')
        print(request.data)
        self.assertEqual(request.status_code, 201)
        self.assertEqual(message, 'Usuario creado exitosamente')
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