from django.contrib.auth.models import BaseUserManager

class ManejoCliente(BaseUserManager):

    def create_user(self,nombre,apellido,email,tipo,documento,celular,password):
        '''Email'''
        if not email:
            raise ValueError('El usuario tiene que tener un correo valido')

        email = self.normalize_email(email)
        # para que ya sea minus o mayus se convierta a minúscula para no tener errores de tipeo
        usuarioCreado = self.model(clienteNombre = nombre,clienteApellido = apellido,clienteCorreo = email, clienteTipo = tipo,clienteDocumento = documento,clienteCelular = celular,password=None)

        if usuarioCreado.clienteTipo ==1:
            usuarioCreado.is_superuser = True

        usuarioCreado.set_password(password)
        usuarioCreado.save(using = self.db)

        return usuarioCreado

    def create_superuser(self,clienteNombre,clienteApellido,clienteCorreo,clienteTipo,clienteDocumento,clienteCelular,password ):
        '''Superusuario'''
        # los parametros que va a recibir tienen que ser los mismos que hubiesemos declarado en el usuarioModel REQUIRED_FIELD y en el USERNAME_FIELD , llegaran con esos mismo nombre de parametros y en el caso que se escribiese mal, lanzara un error de argumento inesperado
        nuevoUsuario = self.create_user(
           clienteNombre,clienteApellido,clienteCorreo,clienteTipo,clienteDocumento,clienteCelular, password)

        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True