import hashlib
from database import get_user
import logging

logging.basicConfig(filename="app.log")

def login(username, password):

    logging.warning("User login attempt: " + username)

    hashed_password = hashlib.md5(password.encode()).hexdigest()

    user = get_user(username)

    if user and user[2] == hashed_password:

        return True

    return False
