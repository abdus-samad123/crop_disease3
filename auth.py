import pickle
import os

USER_FILE = "users.pkl"

# Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}

    with open(USER_FILE, "rb") as f:
        return pickle.load(f)

def save_users(users):
    with open(USER_FILE, "wb") as f:
        pickle.dump(users, f)

# ---------------- USER REGISTER ----------------

def register(username, password, question, answer):
    users = load_users()

    if username in users:
        return False, "User already exists"

    users[username] = {
        "password": password,
        "question": question,
        "answer": answer.lower()
    }

    save_users(users)

    return True, "Registration successful"

# ---------------- USER LOGIN ----------------

def login(username, password):
    users = load_users()

    if username not in users:
        return False, "User not found"

    if users[username]["password"] != password:
        return False, "Wrong password"

    return True, "User login successful"

# ---------------- ADMIN LOGIN ----------------

def admin_login(username, password):

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True, "Admin login successful"

    return False, "Invalid admin credentials"

# ---------------- SECURITY QUESTION ----------------

def get_security_question(username):
    users = load_users()

    return users.get(username, {}).get("question")

# ---------------- RESET PASSWORD ----------------

def reset_password(username, answer, new_password):
    users = load_users()

    if username not in users:
        return False, "User not found"

    if users[username]["answer"] != answer.lower():
        return False, "Wrong answer"

    users[username]["password"] = new_password

    save_users(users)

    return True, "Password reset successful"

# ---------------- TESTING ----------------

if __name__ == "__main__":

    # Admin Login Test
    status, msg = admin_login("admin", "admin123")
    print(msg)

    # User Register Test
    register("samad", "1234", "Pet name?", "cat")

    # User Login Test
    status, msg = login("samad", "1234")
    print(msg)
