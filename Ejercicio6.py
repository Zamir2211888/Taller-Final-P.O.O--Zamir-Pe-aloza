#Ejercicio 6 Zamir Peñaloza/2211888

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_informacion(self):
        print(f"Código: {self.codigo}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Stock: {self.stock}")
        
    def calcular_total(self, cantidad):
        return self.precio * cantidad


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al inventario.")

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_stock(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto:
            producto.stock += cantidad
            print(f"Stock actualizado para el producto '{producto.nombre}'.")
        else:
            print("Producto no encontrado en el inventario.")

    def generar_informe_inventario(self):
        print("Informe de inventario:")
        for producto in self.productos:
            producto.mostrar_informacion()
            
    #Metodo Nuevo 
    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None 

class Venta:
    def __init__(self, inventario):
        self.inventario = inventario
        self.productos_vendidos = []
        self.total_venta = 0

    def agregar_producto(self, codigo, cantidad):
        producto = self.inventario.buscar_producto(codigo)
        if producto and producto.stock >= cantidad:
            self.productos_vendidos.append((producto, cantidad))
            self.total_venta += producto.precio * cantidad
            producto.stock -= cantidad
            print(f"Producto '{producto.nombre}' agregado a la venta.")
        else:
            print("Producto no encontrado en el inventario o stock insuficiente.")

    def generar_factura(self):
        print("Factura de venta:")
        for producto, cantidad in self.productos_vendidos:
            print(f"Producto: {producto.nombre} - Cantidad: {cantidad}")
        print(f"Total venta: {self.total_venta}")


# Ejemplo de uso
inventario = Inventario()

producto1 = Producto("001", "Camiseta", 60000, 10)
producto2 = Producto("002", "Pantalón", 120000, 5)
producto3 = Producto("003", "Zapatos", 150000, 3)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

inventario.generar_informe_inventario()

venta = Venta(inventario)

venta.agregar_producto("001", 2)
venta.agregar_producto("002", 1)
venta.agregar_producto("003", 1)
venta.generar_factura()

#Implementacion metodo nuevo
producto_encontrado = inventario.buscar_producto_por_nombre("Zapatos")
if producto_encontrado:
    print("Producto Encontrado:" )
    producto_encontrado.mostrar_informacion()
else:
    print("Producto no encontrado.")


