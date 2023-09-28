import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="Selecione uma pasta") 

path_file = os.listdir(path)

locais = {
    "imagens": [".png", ".jpng", "jfif", ".gif", ".tfif", ".svg", "jpeg", ".bmp"],
    "planilhas": [".xlsx"],
    "pdfs": [".pdf"],
    "csv": ["csv"],
}

for file in path_file:
    nome, extensao = os.path.split(f"{path}/{file}")
    for folder in locais: 
        if extensao in locais[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"path/{folder}", f"{path}/{folder}/{file}")