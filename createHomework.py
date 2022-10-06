# Create homework

# Import modules
import os

# Enter folder name
folder = input("Folder name: ")

# Current path
path = os.getcwd()

# Homeworks path
homeworksPath = os.path.join(path, 'Tareas')

# Homework path
homeworkPath = os.path.join(homeworksPath, folder)

# Validate if homework path exists
if os.path.exists(homeworkPath):
    print("The folder already exists")
else:
    # Enter homework description
    description = input("Description: ")
    # Create homeworks folder
    os.mkdir(homeworkPath)

    # Create homework file
    filePy = folder.replace(' ', '_') + '.py'
    fileMD = folder.replace(' ', '_') + '.md'

    # Create file
    open(os.path.join(homeworkPath, filePy), 'w').close()

    # Open homework fileMD and write description
    with open(os.path.join(homeworkPath, fileMD), 'w') as file:
        file.write('# ' + folder + '\n')
        file.write('Descripcion: ' + description + '\n' + '\n')
        file.write('## Ejemplo: ' + '\n' + '\n')
        file.write('```code' + '\n')
        
        while True:
            ejemplo = input("Ejemplo: ")

            if ejemplo == '': break

            file.write(ejemplo + '\n')

        file.write('```')
        file.close()
