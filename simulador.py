from faker import Faker 
fake = Faker()

def fake_products(cantidad):
    UNIDADES_MEDIDAS = ['UN']

    for id in range(1, cantidad+1):
        nombre = "Producto "+str(id)
        descripcion = "Descripcion "+str(id)
        precio = float(fake.pydecimal(left_digits=3, right_digits=2,
                        positive=True, min_value=1, max_value=125))
        unidad_medida = UNIDADES_MEDIDAS[fake.random_int(min=0, max=0)]
        print("INSERT INTO productos (nombre, descripcion, precio, unidad_medida, estado) VALUES ('%s', '%s', %s, '%s', true);" % (
            nombre, descripcion, precio, unidad_medida))

fake_products(100)
 