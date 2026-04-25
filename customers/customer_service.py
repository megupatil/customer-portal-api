import os

def search_customer(name):

    command = "grep " + name + " customers.txt"

    result = os.system(command)

    return result
