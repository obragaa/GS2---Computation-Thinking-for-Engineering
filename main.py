"""
Beep Beep

O preço da locação varia de acordo com as informações abaixo:

    - A partir de 6 horas: R$ 4,90 mais R$ 0,40 (por minuto)
    - A partir de 12 horas: R$ 4,90 mais R$ 0,30 (por minuto)
    - A partir de 24 horas: R$ 4,90 mais R$ 0,20 (por minuto)
    - A partir de 48 horas: R$ 4,90 mais R$ 0,18 (por minuto)
"""

carros = ["Renault Zoe", "CAOA Chery Arrizo 5e"]
preco_base = 4.90
preco_final = preco_base
contador = 0

print("Os carros disponíveis para locação são:")
for i in carros:
    print(f"({contador}) - {i}")
    contador += 1
print("-" * 40)
try:
    num_modelo_escolhido = int(input("Escolha o seu modelo: "))
    modelo_escolhido = carros[num_modelo_escolhido]
    tempo_de_utilizacao = float(input("Digite o tempo para locação em horas: "))
except:
    print("Você não digitou corretamente, tente novamente!")
    exit()

if tempo_de_utilizacao <= 6:
    print("1")
    preco_final = preco_base

elif tempo_de_utilizacao > 6 and tempo_de_utilizacao <= 12:
    preco_aux = tempo_de_utilizacao * 60
    preco_aux = preco_aux * 0.40
    preco_final = preco_base + preco_aux
    
elif tempo_de_utilizacao > 12 and tempo_de_utilizacao <= 24:
    preco_aux = tempo_de_utilizacao * 60
    preco_aux = preco_aux * 0.30
    preco_final = preco_base + preco_aux

elif tempo_de_utilizacao > 24 and tempo_de_utilizacao <= 48:
    preco_aux = tempo_de_utilizacao * 60
    preco_aux = preco_aux * 0.20
    preco_final = preco_base + preco_aux

else:
    preco_aux = tempo_de_utilizacao * 60
    preco_aux = preco_aux * 0.18
    preco_final = preco_base + preco_aux

texto_arquivo = f"O aluguel do carro eletrico {modelo_escolhido}, no periodo de {tempo_de_utilizacao}h, ficara no valor de R${preco_final}."

arquivo = open("resumo-aluguel.txt", "w")
arquivo.write(texto_arquivo)
arquivo.close()