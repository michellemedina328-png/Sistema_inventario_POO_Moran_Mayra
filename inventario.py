"""
Clase Inventario
Gestiona la lista de productos.
"""

from producto import Producto


class Inventario:
    def __init__(self):
        self.productos = []

    # =============================
    # Añadir producto
    # =============================
    def agregar_producto(self, producto):
        # Validar ID único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente.")

    # =============================
    # Eliminar producto
    # =============================
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("🗑 Producto eliminado.")
                return
        print("❌ Producto no encontrado.")

    # =============================
    # Actualizar producto
    # =============================
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("✏ Producto actualizado.")
                return
        print("❌ Producto no encontrado.")

    # =============================
    # Buscar por nombre
    # =============================
    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron coincidencias.")

    # =============================
    # Mostrar todos
    # =============================
    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
            return

        print("\n=== INVENTARIO ===")
        for p in self.productos:
            print(p)
