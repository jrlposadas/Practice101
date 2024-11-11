import database

def sign_up_user(full_name, contact_no, email, username, password):
    try:
        database.add_user(full_name, contact_no, email, username, password)
        return True
    except Exception as e:
        print("Error signing up:", e)
        return False

def login_user(username, password):
    # Attempt to authenticate the user with the given credentials
    user = database.authenticate(username, password)
    return user is not None
