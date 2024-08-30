class Compra:
    def __init__(self):
        self.productos_comprados = []  # Lista para almacenar los productos comprados

    def registrar_compra(self):
        print("\n--- Registro de Compras ---")
        total_compra = 0
        while True:
            producto = input("Ingresa el nombre del producto: ")
            precio = float(input("Ingresa el precio del producto: "))
            total_compra += precio
            self.productos_comprados.append({'nombre': producto, 'precio': precio})  # Añade el producto a la lista
            otro_producto = input("¿Deseas agregar otro producto? (si/no): ").lower()
            if otro_producto != 'si':
                break

        print("\n--- Detalle de la Compra ---")
        for item in self.productos_comprados:
            print(f"Producto: {item['nombre']}, Precio: ${item['precio']:.2f}")

        print(f"\nTotal de la compra: ${total_compra:.2f}")
        efectivo = float(input("Ingresa el efectivo recibido: "))
        vuelto = efectivo - total_compra
        print(f"Vuelto a entregar: ${vuelto:.2f}")


class Proveedor:
    def __init__(self):
        self.productos_proveedores = []  # Lista para almacenar los productos de proveedores

    def gestionar_proveedores(self):
        print("\n--- Registrar productos de Proveedores ---")
        while True:
            producto = input("Ingresa el nombre del producto recibido: ")
            precio_sugerido = float(input("Ingresa el precio sugerido de venta: "))
            self.productos_proveedores.append({'nombre': producto, 'precio': precio_sugerido})
            otro_producto = input("¿Deseas registrar otro producto? (si/no): ").lower()
            if otro_producto != 'si':
                break

        print("\n--- Productos Ingresados ---")
        for producto in self.productos_proveedores:
            print(f"Producto: {producto['nombre']}, Precio Sugerido: ${producto['precio']:.2f}")


class Tienda:
    def __init__(self):
        self.compra = Compra()
        self.proveedor = Proveedor()

    def menu_principal(self):
        while True:
            print("\n--- Tienda de Niña Mary ---")
            print("1. Registrar Compra")
            print("2. Registrar productos de Proveedores")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.compra.registrar_compra()
            elif opcion == '2':
                self.proveedor.gestionar_proveedores()
            elif opcion == '3':
                print("¡Has salido del sistema!")
                break
            else:
                print("Opción no válida, por favor intenta de nuevo.")


# Ejecución del programa
tienda = Tienda()
tienda.menu_principal()

#en este codigo se utilizo el poo para la creacion de clases y gracias al poo 
#se puede hacer uso de la reutilizacion de las clases 

#esete programa le ayuda a niña mary a registrar los productos que compraron los clientes en listarlos y
#  hacer la suma de los precios y darle un total 
#tambien se agrego una opcion para que cuando niña mary reciba mercaderia pueda registrarla y agregar el precio sugerido de venta
