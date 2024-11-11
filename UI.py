import flet as ft
import PAL

def display_login(page):
    def login_action(e):
        username = username_input.value
        password = password_input.value
        if PAL.login(username, password):
            page.controls.clear()
            success_text.value = f"Login successful! Welcome {username}!"
            page.update()
            display_select_route(page, username)
        else:
            error_text.value = "Invalid username or password."
            page.update()

    def switch_to_signup(e):
        page.controls.clear()
        display_signup(page)
        page.update()

    username_input = ft.TextField(label="User Name:")
    password_input = ft.TextField(label="Password:", password=True)
    error_text = ft.Text(color="red")
    success_text = ft.Text(color="green")

    page.controls.append(ft.Column([
        ft.Text("Welcome to EASYBUS!", size=30, weight="bold"),
        ft.Text("Your Personal Bus Ticket Booking App", size=18),
        username_input,
        password_input,
        ft.ElevatedButton("Log In", on_click=login_action),
        error_text,
        success_text,
        ft.TextButton("No account yet? Sign Up", on_click=switch_to_signup)
    ]))

    page.update()

def display_signup(page):
    def signup_action(e):
        full_name = full_name_input.value
        contact_no = contact_input.value
        email = email_input.value
        username = username_input.value
        password = password_input.value
        if PAL.sign_up(full_name, contact_no, email, username, password):
            success_text.value = "Account successfully created! Please log in."
            page.controls.clear()
            display_login(page)
        else:
            error_text.value = "Sign-up failed. Username might already exist."
        page.update()

    def switch_to_login(e):
        page.controls.clear()
        display_login(page)
        page.update()

    full_name_input = ft.TextField(label="Full Name:")
    contact_input = ft.TextField(label="Contact No (Optional):")
    email_input = ft.TextField(label="Email Address:")
    username_input = ft.TextField(label="Username:")
    password_input = ft.TextField(label="Password:", password=True)
    error_text = ft.Text(color="red")
    success_text = ft.Text(color="green")

    page.controls.append(ft.Column([
        ft.Text("Create a New Account", size=30, weight="bold"),
        full_name_input,
        contact_input,
        email_input,
        username_input,
        password_input,
        ft.ElevatedButton("Create Account", on_click=signup_action),
        ft.ElevatedButton("Back to Login", on_click=switch_to_login),
        error_text,
        success_text
    ]))

    page.update()

def display_select_route(page, username):
    locations = ["Batangas", "Cavite", "Manila", "Subic"]

    starting_location = ft.Dropdown(
        label="Starting Location:",
        options=[ft.dropdown.Option(loc) for loc in locations]
    )

    destination = ft.Dropdown(
        label="Destination:",
        options=[ft.dropdown.Option(loc) for loc in locations]
    )

    def next_action(e):
        if starting_location.value == destination.value:
            error_text.value = "Starting location and destination cannot be the same."
            page.update()
        else:
            route = f"{starting_location.value} to {destination.value}"
            page.controls.clear()
            display_booking_details(page, route)
            page.update()

    error_text = ft.Text(color="red")

    page.controls.append(ft.Column([
        ft.Text("Select Your Route", size=30, weight="bold"),
        starting_location,
        destination,
        ft.ElevatedButton("Next", on_click=next_action),
        error_text
    ]))

    page.update()

def display_booking_details(page, route, fare_per_seat=45.78, available_seats=41):
    selected_seat = ft.Dropdown(
        label="Select # of Seats:",
        options=[ft.dropdown.Option(str(i)) for i in range(1, available_seats + 1)]
    )
    
    total_fare_text = ft.Text("Total Fare: ")
    def update_total_fare(e):
        if selected_seat.value:
            total_fare = fare_per_seat * int(selected_seat.value)
            total_fare_text.value = f"Total Fare: ₱{total_fare:.2f}"
            page.update()
    
    selected_seat.on_change = update_total_fare
    
    def confirm_booking(e):
        page.controls.clear()
        page.controls.append(ft.Text("Booking confirmed successfully!", size=25, weight="bold"))
        page.update()

    page.controls.append(ft.Column([
        ft.Text("Booking Details", size=40, weight="bold"),
        ft.Text(f"Route: {route}"),
        ft.Text("Departure Time: 08:00"),
        ft.Text("Arrival Time: 10:00"),
        ft.Text(f"Fare per Seat: ₱{fare_per_seat:.2f}"),
        ft.Text(f"Available Seats: {available_seats}"),
        selected_seat,
        total_fare_text,
        ft.ElevatedButton("Confirm Booking", on_click=confirm_booking)
    ]))

    page.update()
