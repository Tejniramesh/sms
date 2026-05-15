import bcrypt
from utils.db import users_collection

def register_user(username, email, password):

    existing_user = users_collection.find_one({"email": email})

    if existing_user:
        return False

    hashed_password = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    users_collection.insert_one({
        "username": username,
        "email": email,
        "password": hashed_password
    })

    return True

def login_user(email, password):

    user = users_collection.find_one({"email": email})

    if not user:
        return False

    return bcrypt.checkpw(
        password.encode("utf-8"),
        user["password"]
    )
