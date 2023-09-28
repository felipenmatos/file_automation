import PyPDF2
import os

merger = PyPDF2.PdfMerger() #pdf file handler

lista_arquivos = os.listdir("arquivos") #check all files at this address
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"arquivos/{arquivo}") #whatever file must be merged

merger.write("merged_pdf.pdf") #saving the merged pdf


