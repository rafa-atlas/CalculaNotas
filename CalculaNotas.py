from funcoes import media_ponderada

# Apresentação
print("Programa para calcular a média ponderada de três avaliações.")
print("")

# Entrada de dados
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Processamento
media = media_ponderada(nota1, nota2, nota3)

# Saída de dados
print(f"A média ponderada das avaliações é {media}.")