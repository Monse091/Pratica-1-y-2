from producto import Producto
from super_mercado import Super_mercado
import random
import flet as ft
# Función para generar un nombre de producto básico (producto1, producto2, ...)
def generar_nombre_producto(num_producto):
    return f"producto{num_producto}"

# Función para generar un producto con cantidad y precio aleatorios
def generar_producto(num_producto):
    nombre = generar_nombre_producto(num_producto)
    cantidad = random.randint(1, 100)
    precio = round(random.uniform(0.5, 100.0), 2)
    return Producto(nombre, cantidad, precio)

def main(page: ft.page):
    def handle_Eliminar(e):
        indice=input_Eliminar.value
        supermercado.retirar_producto(int(indice))

        lista_No_disponible=supermercado.mostrar_inventario_retirados()
        columna_No_disponible.controls.clear()
        for i in range(len(lista_No_disponible)):
            columna_No_disponible.controls.append(ft.Text(lista_No_disponible[i]))

        lista_Disponible=supermercado.mostrar_inventario_disponible()
        columna_disponible.controls.clear()
        for i in range(len(lista_Disponible)):
            columna_disponible.controls.append(ft.Text(lista_Disponible[i]))

        page.update()



    supermercado = Super_mercado()
    columna_disponible =ft.Column()
    columna_No_disponible =ft.Column()
    btn_Eliminar =ft.ElevatedButton("Eliminar",on_click=handle_Eliminar)
    input_Eliminar  =ft.TextField(label="Indice de producto a eliminar")

    # Generar 10 productos y agregarlos al supermercado
    for i in range(1, 11):
        producto = generar_producto(i)
        supermercado.agregar_producto(producto)

    lista_Disponible=supermercado.mostrar_inventario_disponible()
    lista_No_disponible=supermercado.mostrar_inventario_retirados()

    for i in range(len(lista_Disponible)):
        columna_disponible.controls.append(ft.Text(lista_Disponible[i]))
    for i in range(len(lista_No_disponible)):
        columna_No_disponible.controls.append(ft.Text(lista_No_disponible[i]))



    
    contenedorPrincipal=ft.Container(
        ft.Row([
            ft.Column([
                ft.Text("Productos_Disponibles",size=20,weight="bold"),
                ft.Container(columna_disponible)
            ]),
            ft.Column([
                ft.Text("Productos_No_disponibles",size=20,weight="bold"),
                ft.Container(columna_No_disponible)
            ]),
        ],alignment=ft.MainAxisAlignment.SPACE_AROUND),
         alignment=ft.alignment.top_center, border=ft.border.all(5,color="white"),padding=20
    )


    page.add(
        ft.AppBar(
        leading_width=30, title=ft.Text("Super Mercado"),
        center_title=False,
        bgcolor=ft.colors.BLUE_ACCENT_700),
        contenedorPrincipal, input_Eliminar, btn_Eliminar

    )

ft.app(main)