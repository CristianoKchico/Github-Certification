# Recebe a string e repete quantas vezes solicitado.

string = input("Digite a string a ser repetida: ")
numero = int(input("Digite o número de veszes para repetir a string: "))

print((string + ' ') * numero)
print(f"Sua string '{string}' foi repetida {numero} vezes.")