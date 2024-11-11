import sqlite3

def create_table():
    try:
        # Connect to the database (creates the file if it doesn’t exist)
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        
        # Create the users table if it doesn’t exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                full_name TEXT,
                contact_no TEXT,
                email TEXT,
                username TEXT PRIMARY KEY,
                password TEXT
            )
        """)
        conn.commit()

        # Add a default admin user
        cursor.execute("SELECT * FROM users WHERE username = ?", ("admin123",))
        if not cursor.fetchone():
            cursor.execute("INSERT INTO users (full_name, contact_no, email, username, password) VALUES (?, ?, ?, ?, ?)",
                           ("Admin", "0000000000", "admin@example.com", "admin123", "password"))
            conn.commit()

        print("Database and table created successfully.")
    except sqlite3.Error as e:
        print("Error creating table:", e)
    finally:
        conn.close()

def add_user(full_name, contact_no, email, username, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (full_name, contact_no, email, username, password) VALUES (?, ?, ?, ?, ?)",
                       (full_name, contact_no, email, username, password))
        conn.commit()
    except sqlite3.Error as e:
        print("Error adding user:", e)
    finally:
        conn.close()

def authenticate(username, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        return user
    except sqlite3.Error as e:
        print("Error authenticating user:", e)
        return None
    finally:
        conn.close()
