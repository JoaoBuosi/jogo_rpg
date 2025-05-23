import flet as ft
import time
import os

from src.personagens import character_customization_screen


def main(page: ft.Page):
    page.title = "Meu Jogo"
    page.window_width = 580
    page.window_height = 860
    page.window_resizable = False
    page.bgcolor = "black"
    page.padding = 0
    page.spacing = 0

    largura = 566
    altura = 838

    def ir_para(tela):
        if tela == "login":
            mostrar_tela("login_screen.png")
            page.dialog = ft.AlertDialog(
                title=ft.Text("Login feito!"),
                on_dismiss=lambda _: ir_para_loading("character")
            )
            page.dialog.open = True

        elif tela == "register":
            mostrar_tela("register_screen.png")
            page.dialog = ft.AlertDialog(
                title=ft.Text("Cadastro feito!"),
                on_dismiss=lambda _: ir_para_loading("character")
            )
            page.dialog.open = True

        elif tela == "game":
            ir_para_loading("jogo")

        page.update()

    def ir_para_loading(destino):
        mostrar_tela("loading_screen.png")
        page.update()
        time.sleep(2)

        if destino == "character":
            page.views.clear()
            page.views.append(character_customization_screen(page))
        else:
            mostrar_tela("game.png")

        page.update()

    def mostrar_tela(nome_arquivo):
        page.views.clear()

        caminho = f"assets/{nome_arquivo}"
        if not os.path.exists(caminho):
            print(f"❌ Arquivo não encontrado: {caminho}")
            return

        elementos = [
            ft.Image(
                src=caminho,
                width=largura,
                height=altura,
                fit=ft.ImageFit.FILL
            )
        ]

        if nome_arquivo == "initial_page.png":
            elementos += [
                ft.Container(
                    width=200, height=50,
                    top=580, left=180,
                    bgcolor="transparent",
                    on_click=lambda _: ir_para("login")
                ),
                ft.Container(
                    width=200, height=50,
                    top=640, left=180,
                    bgcolor="transparent",
                    on_click=lambda _: ir_para("register")
                ),
                ft.Container(
                    width=200, height=50,
                    top=700, left=180,
                    bgcolor="transparent",
                    on_click=lambda _: ir_para("game")
                ),
            ]

        page.views.append(
            ft.View(
                route="/",
                controls=[
                    ft.Stack(
                        controls=elementos,
                        width=largura,
                        height=altura
                    )
                ]
            )
        )
        page.update()

    mostrar_tela("initial_page.png")

ft.app(target=main)

