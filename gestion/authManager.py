from django.contrib.auth.models import BaseUserManager

class ManejoCliente(BaseUserManager):

    def create_user(self,nombre,documento,celular,correo,perfilCliente,password = None):
        if not correo:
            raise ValueError('El usuario tiene que tener un correo valido')
        if not celular:
            raise ValueError('El usuario tienen que tener un correo valido')
        
        correo = self.normalize_email(correo)

        usuarioCreado = self.model(clienteNombre = nombre,clienteDocumento = documento,clienteCelular = celular,clienteCorreo = correo,perfilCliente= perfilCliente, clientePassword =password)

        usuarioCreado.set_password(password)
        usuarioCreado.save(using = self.db)
        return usuarioCreado
    
    def create_superuser(self,nombre,documento,celular,correo,perfilCliente,password = None):
        nuevoUsuario = self.create_user(
           nombre,documento,celular,correo,perfilCliente, password)

        nuevoUsuario.is_superuser = True
        # nuevoUsuario.is_staff = True
        nuevoUsuario.save(using=self._db)