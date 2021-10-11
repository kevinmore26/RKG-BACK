from rest_framework.test import APITestCase
from .models import ClienteModel

# Create your tests here.

class ClienteTestCase(APITestCase):
    def setUp(self):
        ClienteModel(
            clienteNombre = "PruebaNombre1",
            clienteApellido = "PruebaApellido1",
            clienteDocumento = "12345678",
            clienteCelular = "912345678",
            clienteCorreo = "Testcorreo1@hotmail.com",
            password = "ClavePrueba1",
            clienteTipo = 1
        ).save()
        ClienteModel(
            clienteNombre = "PruebaNombre2",
            clienteApellido = "PruebaApellido2",
            clienteDocumento = "22345678",
            clienteCelular = "922345678",
            clienteCorreo = "Testcorreo2@hotmail.com",
            password = "ClavePrueba2",
            clienteTipo = 2
        ).save()
        ClienteModel(
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
        
    # def test_post_client_exists_fail(self):
    #     '''Deberia arrojar un error si el cliente ya existe'''
    #     nuevoCliente = {
    #         "clienteNombre" : "PruebaNombre1",
    #         "clienteApellido" : "PruebaApellido1",
    #         "clienteDocumento" : "12345678",
    #         "clienteCelular" : 912345678 ,
    #         "clienteCorreo" : "Testcorreo1@hotmail.com",
    #         "clienteTipo" : 1
    #     }

    #     self.client.post(
    #         '/gestion/clientes/', data=nuevoCliente, format='json')

    #     request = self.client.post(
    #         '/gestion/clientes/', data=nuevoCliente, format='json')

    #     self.assertEqual(request.status_code, 400)