import os
import time
from termcolor import colored
from subprocess import run

name = input(colored("Enter the name of your project => ", "green"))
extension = input(colored("Enter File extenstion for your language =>", "green"))
editor = input(colored("Which editor do you want to use => ", "green"))

path = "/home/risen/atom/electron/"
folder_path = os.path.join(path, name)
os.mkdir(folder_path)

print(colored("[CREATED FOLDER]", "blue"))

file_path = os.path.join(folder_path, f"app.{extension}")
open(file_path, "w").close()

print(colored("[CREATED FILE]", "blue"))


if editor == "nvim":
    print(colored("[OPENING NVIM]", "blue"))
    time.sleep(2)

    run(["nvim", file_path])
elif editor == "vsc":
     print(colored("[OPENING Visual Studio Code]", "blue"))
     time.sleep(2)

     run(["code", file_path])
