from django.contrib.auth.models import BaseUserManager

class ManejoCliente(BaseUserManager):

    def create_user(self,nombre,apellido,documento,celular,correo,tipo,password = None):
        if not correo:
            raise ValueError('El usuario tiene que tener un correo valido')
        
        if not celular:
            raise ValueError('El usuario tienen que tener un correo valido')
        
        correo = self.normalize_email(correo)

        usuarioCreado = self.model(
        clienteNombre = nombre, clienteApellido = apellido,
        clienteDocumento = documento,clienteCelular = celular,
        clienteCorreo = correo,clienteTipo=tipo
        )
        usuarioCreado.set_password(password)
        usuarioCreado.save(using = self.db)

        return usuarioCreado
    
    def create_superuser(self,clienteNombre,clienteApellido,clienteDocumento,clienteCelular,clienteCorreo,password,clienteTipo):
        nuevoUsuario = self.create_user(
           clienteNombre,
           clienteApellido,
           clienteDocumento,
           clienteCelular,
           clienteCorreo,
           password,
           clienteTipo
        )

        nuevoUsuario.is_superuser = True
        nuevoUsuario.is_staff = True
        nuevoUsuario.save(using=self._db)