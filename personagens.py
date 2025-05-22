import flet as ft

def character_customization_screen(page: ft.Page):
    nome = ft.TextField(label="Nome do Personagem", width=300)
    
    cabelo = ft.Dropdown(
        label="Cabelo",
        options=[
            ft.dropdown.Option("Curto"),
            ft.dropdown.Option("Longo"),
            ft.dropdown.Option("Cacheado"),
            ft.dropdown.Option("Careca")
        ],
        width=300
    )

    cor_pele = ft.Dropdown(
        label="Cor da Pele",
        options=[
            ft.dropdown.Option("Clara"),
            ft.dropdown.Option("Morena"),
            ft.dropdown.Option("Negra"),
            ft.dropdown.Option("Fantasma")
        ],
        width=300
    )

    forca = ft.Slider(min=1, max=10, divisions=9, label="Força: {value}", width=300)
    inteligencia = ft.Slider(min=1, max=10, divisions=9, label="Inteligência: {value}", width=300)

    def salvar_personagem(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Personagem salvo!"),
            content=ft.Text(f"{nome.value} personalizado com sucesso."),
            actions=[ft.TextButton("OK", on_click=lambda _: page.dialog.close())]
        )
        page.dialog.open = True
        page.update()

    def voltar(e):
        page.go("/login")

    return ft.View(
        "/character_customization",
        controls=[
            ft.Column([
                ft.Text("Personalização do Personagem", size=22, weight="bold"),
                nome,
                cabelo,
                cor_pele,
                ft.Text("Força"),
                forca,
                ft.Text("Inteligência"),
                inteligencia,
                ft.Row([
                    ft.ElevatedButton("Salvar", on_click=salvar_personagem),
                    ft.TextButton("Voltar", on_click=voltar),
                ], alignment="spaceBetween")
            ], alignment="center", horizontal_alignment="center")
        ],
        padding=20,
        scroll=ft.ScrollMode.AUTO
    )

if __name__ == "__main__":
    import flet as ft
    ft.app(target=character_customization_screen)