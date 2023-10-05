import os

title = "----------------\n  FILE RENAMER  \n----------------"
print(title)

files = []

while len(files) == 0:
    path = input("\nWhich directory do you want to work in? ")
    search = input("\nWhich string do you want to replace? ")
    os.chdir(path)
    all_files = os.listdir()
    files = [file for file in all_files if os.path.isfile(file) and search in file]
    if len(files) == 0:
        print("\nNo such files have been found!")

print("\nFound the following files:")
print(", ".join(files))

target = input(f'\nWhich string should "{search}" become? ')

new_names = []
for file in files:
    new_name = file.replace(search, target)
    try:
        os.rename(file, new_name)
        new_names.append(new_name)
    except:
        print(f'\nCould not find "{file}" anymore.')

print("\nThe new names are:")
print(", ".join(new_names))
