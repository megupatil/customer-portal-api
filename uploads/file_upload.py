import os

UPLOAD_FOLDER = "/tmp/uploads"

def save_file(filename, content):

    path = UPLOAD_FOLDER + "/" + filename

    with open(path, "wb") as f:

        f.write(content)
