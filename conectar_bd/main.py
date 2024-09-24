import flet as ft 
from Telas.TelaCadastro import CadastroScreen
def main(page: ft.Page):
    splash_screen = CadastroScreen(page)
    splash_screen.show()
ft.app(target=main)