import random
import flet as ft
import math
from lista_enlazada import ListaEnlazada


def main(page: ft.Page):
    def generate_randoms(e):
        # aqui se Limpia contenido de las columnas
        columna_impar.controls.clear()
        columna_par.controls.clear()
        columna_principal.controls.clear()
        lista_DNumeros_pares = ListaEnlazada()
        lista_DNumeros_impares = ListaEnlazada()
        numeros_aleatorios = [random.randint(1, 100) for _ in range(40)]

        for i in range(len(numeros_aleatorios)):
            if i % 5 == 0:
                columna_principal.controls.append(ft.Row())

            columna_principal.controls[math.trunc(i/5)].controls.append(ft.Container(ft.Text(numeros_aleatorios[i], size=15), width=40, height=40, alignment=ft.alignment.center, border=ft.border.all(5)))

        # ordenamos los pares e impares
        for numero in numeros_aleatorios:
            if numero % 2 == 0:
                lista_DNumeros_pares.agregar_elemento(numero)
            else:
                lista_DNumeros_impares.agregar_elemento(numero)

        # conseguimos las listas de los números
        pares = lista_DNumeros_pares.get_lista()
        impares = lista_DNumeros_impares.get_lista()

        for i in range(len(pares)):
            if i % 5 == 0:
                columna_par.controls.append(ft.Row())

            columna_par.controls[math.trunc(i/5)].controls.append(ft.Container(ft.Text(pares[i], size=15), width=40, height=40, alignment=ft.alignment.center, border=ft.border.all(5)))
    

        for i in range(len(impares)):
            if i % 5 == 0:
                columna_impar.controls.append(ft.Row())

            columna_impar.controls[math.trunc(i/5)].controls.append(ft.Container(ft.Text(impares[i], size=15), width=40, height=40, alignment=ft.alignment.center,border=ft.border.all(5)))

        page.update()
        
    columna_par = ft.Column(scroll=ft.ScrollMode.ALWAYS)
    columna_impar = ft.Column(scroll=ft.ScrollMode.ALWAYS)
    columna_principal = ft.Column(scroll=ft.ScrollMode.ALWAYS)


    container = ft.Container(ft.Row([
        ft.Column([ft.Text("Lista Original", weight="bold", size=20,color=ft.colors.CYAN_300), ft.Container(columna_principal, margin=ft.margin.only(bottom=25))]),
        ft.Column([ft.Text("pares", weight="bold", size=20, color=ft.colors.CYAN_300), ft.Container(columna_par, margin=ft.margin.only(bottom=25))]),
        ft.Column([ft.Text("impares", weight="bold", size=20,color=ft.colors.CYAN_300), ft.Container(columna_impar, margin=ft.margin.only(bottom=25))]),
    ], alignment="center", spacing=20, height=400)
    )

    page.add(
         ft.Container(ft.ElevatedButton("crear números", on_click=generate_randoms), alignment=ft.alignment.center),container
    )

ft.app(main)