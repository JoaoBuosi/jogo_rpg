import flet as ft
from src.auth import login_screen, register_screen
from src.personagens import character_customization_screen



def initial_page(page: ft.Page):
    def go_to_login(e):
        page.session.set("next_route", "/login")
        page.go("/loading")

    def go_to_register(e):
        page.session.set("next_route", "/register")
        page.go("/loading")

    def go_to_game(e):
        page.session.set("next_route", "/character_customization")  # ou "/game"
        page.go("/loading")

    return ft.View(
        "/",
        controls=[
            ft.Column([
                ft.Image(src="assets/Initial_page.png", expand=True, fit=ft.ImageFit.CONTAIN),
                ft.ElevatedButton("Login", on_click=go_to_login),
                ft.ElevatedButton("Cadastrar", on_click=go_to_register),
                ft.ElevatedButton("Iniciar Jogo", on_click=go_to_game),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def loading_screen(page: ft.Page):
    async def go_next():
        await page.update_async()
        await page.sleep(2)
        next_route = page.session.get("next_route")
        if next_route:
            page.go(next_route)

    page.on_load = lambda _: go_next()

    return ft.View(
        "/loading",
        controls=[
            ft.Column([
                ft.Image(src="assets/loading_screen.png", width=400)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def main(page: ft.Page):
    page.title = "Meu Jogo"
    page.session.set("next_route", None)

    def route_change(route):
        page.views.clear()

        routes = {
            "/": initial_page,
            "/login": login_screen,
            "/register": register_screen,
            "/character_customization": character_customization_screen,
            "/loading": loading_screen,
        }

        view_function = routes.get(page.route, initial_page)
        page.views.append(view_function(page))
        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(target=main, assets_dir="assets")
