def conta_palavras(frase):
    palavras = frase.split(" ")
    return len(palavras)


print(conta_palavras("O rato roeu a roupa do rei de Roma"))
