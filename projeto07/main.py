import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)


locais = {
    "imagens" : [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".cr2", ".nef", ".psd", ".svg", ".ico"],
    "videos" : [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", "webm", ".3gp"],
    "Documentos de texto": [".docx", ".rtf", ".txt", ".odt", ".tex", ".html", ".md",".epub"],
    "planilhas" : [".xls", ".xlsx", ".csv", ".ods", ".gsheet", ".numbers", ".pdf"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")