text1 = set(input().split())
text2 = set(input().split())

# procurar os elementos iguais
set3 = text1 & text2

# fazer o tento para printar
texto = ""
for elemento_comum in set3:
    texto += f"{elemento_comum} "

print(texto.strip())
