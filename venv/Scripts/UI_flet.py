import flet as ft
from PAL import Application

def main(page: ft.Page):
    app = Application()
    
    page.title = "BusBuddy - Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Title and subtitle
    title = ft.Text("Welcome to BusBuddy!", size=24, weight="bold", color="red")
    subtitle = ft.Text("Your Personal Bus Ticket Booking App", size=16, color="gray")
    
    # Input fields
    username_field = ft.TextField(label="User Name:", width=300)
    password_field = ft.TextField(label="Password:", password=True, width=300)
    
    # Feedback message
    message = ft.Text("", color="red")
    
    # Login button click event
    def on_login(e):
        username = username_field.value
        password = password_field.value
        result = app.login_user(username, password)
        if result == "Login successful!":
            message.value = "Welcome!"
            message.color = "green"
        else:
            message.value = "Invalid username or password."
            message.color = "red"
        page.update()
    
    login_button = ft.ElevatedButton(text="Log In", on_click=on_login)
    
    # Adding components to the page
    page.add(title, subtitle, username_field, password_field, login_button, message)

