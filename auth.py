
import flet as ft
import time

def login_screen(page: ft.Page):
    email = ft.TextField(label="Email", width=300)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

    def fazer_login(e):
        page.go("/loading")  # Simula carregamento
        time.sleep(1.5)  # Espera 1.5s
        page.go("/character_customization")

    def ir_para_cadastro(e):
        page.go("/loading")
        time.sleep(1.5)
        page.go("/register")

    return ft.View(
        "/login",
        controls=[
            ft.Image(src="assets/login_screen.png", width=400),
            email,
            senha,
            ft.ElevatedButton("Entrar", on_click=fazer_login),
            ft.TextButton("Cadastrar-se", on_click=ir_para_cadastro),
        ],
        scroll=ft.ScrollMode.AUTO,
        padding=20
    )

def register_screen(page: ft.Page):
    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="Email", width=300)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

    def registrar(e):
        page.go("/loading")
        time.sleep(1.5)
        page.go("/login")

    return ft.View(
        "/register",
        controls=[
            ft.Image(src="assets/register_screen.png", width=400),
            nome,
            email,
            senha,
            ft.ElevatedButton("Registrar", on_click=registrar),
            ft.TextButton("Voltar para o Login", on_click=lambda _: page.go("/login")),
        ],
        scroll=ft.ScrollMode.AUTO,
        padding=20
    )

def loading_screen(page: ft.Page):
    return ft.View(
        "/loading",
        controls=[
            ft.Image(src="assets/loading_screen.png", width=400),
            ft.ProgressRing(),
            ft.Text("Carregando...", size=18)
        ],
        padding=30,
        scroll=ft.ScrollMode.AUTO
    )
