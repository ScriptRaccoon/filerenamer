import os
from termcolor import cprint

title = "----------------\n  FILE RENAMER  \n----------------"
cprint(title, "cyan")

files = []
while len(files) == 0:
    path = input("Which directory do you want to work in? ")
    search = input("Which string do you want to replace? ")
    os.chdir(path)
    all_files = os.listdir()
    files = [file for file in all_files if os.path.isfile(file) and search in file]
    if len(files) == 0:
        cprint("No such files have been found!", "red")

print("Found the following files:")
cprint(", ".join(files), "yellow")
target = input(f'Which string should "{search}" become? ')

new_names = []
for file in files:
    new_name = file.replace(search, target)
    try:
        os.rename(file, new_name)
        new_names.append(new_name)
    except:
        cprint(f'Could not find "{file}" anymore.', "red")

print("The new names are:")
cprint(", ".join(new_names), "green")
