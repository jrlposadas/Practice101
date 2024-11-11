import BL

def sign_up(full_name, contact_no, email, username, password):
    return BL.sign_up_user(full_name, contact_no, email, username, password)

def login(username, password):
    return BL.login_user(username, password)
