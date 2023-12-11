import os
import PyPDF2


merge = PyPDF2.PdfMerger()

lista_de_arquivos = os.listdir("arquivos")

lista_de_arquivos.sort()

for arquivo in lista_de_arquivos:
    if arquivo.endswith(".pdf"):
        merge.append(f"arquivos/{arquivo}")


merge.write("PDF final.pdf")
merge.close()
