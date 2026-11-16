def processar_imagem(caminho):
    with open(caminho, "rb") as arquivo:
        return arquivo.read()
