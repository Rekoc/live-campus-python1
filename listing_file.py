import os
import pathlib


root_file = pathlib.Path(__file__).parent.resolve()

for file in os.listdir(root_file):
    # Liste les fichiers d'un dossier
    # print(file)
    # Ajoutons le chemin d'accès
    path_file = os.path.join(root_file, file)
    read = os.access(path_file, os.R_OK)
    execute = os.access(path_file, os.X_OK)
    write = os.access(path_file, os.W_OK)
    access = oct(os.stat(path_file).st_mode)[-3:]
    print(f"{path_file}\n\tinfo = {access}\n\tread : {read} / write : {write} / execute : {execute}")
    # Combination or 2 :
    read_and_write = os.access(path_file, os.R_OK or os.W_OK)


for root, dirs, files in os.walk(root_file):
    # Do not take hidden files
    files = [f for f in files if not f.startswith(".")]
    # Do not take hidden directories
    dirs = [d for d in dirs if not d.startswith(".")]
    print("----- New dir -----")
    print(f"root = {root}")
    print(f"dirs = {dirs}")
    print(f"files = {files}")
