import sys
import os
from github import Github

path = "C://Users/cagui/Documents/Proyects/MyProjects/" 
#Inserta el directorio donde crearás tu nuevo proyecto

username = "" # <--- Inserta tu github username aquí
password = "" # <--- Inserta tu github password aquí

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()
