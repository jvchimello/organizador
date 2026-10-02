import os
import shutil

def organizar_pasta(caminho_pasta):
    if not os.path.exists(caminho_pasta):
        print(f"A pasta '{caminho_pasta}' não foi encontrada.")
        return

    pasta_xml = os.path.join(caminho_pasta, "XML")
    pasta_pdf = os.path.join(caminho_pasta, "PDF")

    os.makedirs(pasta_xml, exist_ok=True)
    os.makedirs(pasta_pdf, exist_ok=True)

    for arquivo in os.listdir(caminho_pasta):
        caminho_completo = os.path.join(caminho_pasta, arquivo)

        if os.path.isfile(caminho_completo):
            extensao = arquivo.split(".")[-1].lower()

            if extensao == "xml":
                shutil.move(caminho_completo, os.path.join(pasta_xml, arquivo))
                print(f"Movido XML: {arquivo}")
            elif extensao == "pdf":
                shutil.move(caminho_completo, os.path.join(pasta_pdf, arquivo))
                print(f"Movido PDF: {arquivo}")

    print("Organização concluída!")

# Caminho com 'r' antes das aspas para não quebrar a string
caminho = r"G:\Meu Drive\CONSTRUCASA\DANF FORNECEDORES\ANO 2026\MES 10-2026"
organizar_pasta(caminho)
