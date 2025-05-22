import flet as ft
import re


def login_screen(page: ft.Page):
    def go_to_register(e):
        page.go("/loading")
        page.session.set("next_route", "/register")

    def login(e):
        print("Login com:", email.value, senha.value)
        page.go("/loading")
        page.session.set("next_route", "/character_customization")

    email = ft.TextField(label="Email", width=300)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

    return ft.View(
        "/login",
        controls=[
            ft.Image(src="Img.login_screen", width=500),
            ft.Column(
                [
                    ft.Text("LOGIN", size=30, weight="bold"),
                    email,
                    senha,
                    ft.ElevatedButton("Entrar", on_click=login, width=300),
                    ft.TextButton("Criar conta", on_click=go_to_register)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )


def register_screen(page: ft.Page):
    def go_to_login(e):
        page.go("/loading")
        page.session.set("next_route", "/login")

    def register(e):
        if len(nome.value) < 5:
            page.snack_bar = ft.SnackBar(ft.Text("O nome deve ter no mínimo 5 caracteres."), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        if not re.search(r"[A-Z]", senha.value):
            page.snack_bar = ft.SnackBar(ft.Text("A senha deve conter ao menos uma letra maiúscula."), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        if senha.value != confirmar_senha.value:
            page.snack_bar = ft.SnackBar(ft.Text("As senhas não coincidem."), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        print("Cadastro:", nome.value, email.value)
        page.go("/loading")
        page.session.set("next_route", "/character_customization")

    nome = ft.TextField(label="Nome", width=300)
    email = ft.TextField(label="Email", width=300)
    senha = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
    confirmar_senha = ft.TextField(label="Confirmar Senha", password=True, can_reveal_password=True, width=300)

    return ft.View(
        "/register",
        controls=[
            ft.Image(src="Img.register_screen", width=500),
            ft.Column(
                [
                    ft.Text("CRIAR CONTA", size=30, weight="bold"),
                    nome,
                    email,
                    senha,
                    confirmar_senha,
                    ft.ElevatedButton("Registrar", on_click=register, width=300),
                    ft.TextButton("Já tenho conta", on_click=go_to_login)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

if __name__ == "__main__":
    import flet as ft
    ft.app(target=login_screen)
