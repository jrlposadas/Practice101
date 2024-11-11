import flet as ft
import database
import UI

def main(page):
    page.window_width = 500  # Set the width of the window
    page.window_height = 500  # Set the height of the window, making it square
    database.create_table()
    UI.display_login(page)

ft.app(target=main)  # Removed view parameter for compatibility
