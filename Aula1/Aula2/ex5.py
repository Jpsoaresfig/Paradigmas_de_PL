import random

def gerar_cartela_bingo(tamanho=25):
    cartela = []
    numeros_disponiveis = list(range(1, tamanho * tamanho + 1))
    random.shuffle(numeros_disponiveis)

    for i in range(tamanho):
        linha = numeros_disponiveis[i*tamanho:(i+1)*tamanho]
        cartela.append(linha)

    return cartela

def imprimir_cartela(cartela, marcados):
    for linha in cartela:
        print("\t".join(f"{num:02d}{'*' if num in marcados else ''}" for num in linha))

def selecionar_numero(cartela, marcados):
    while True:
        numero = random.choice(random.choice(cartela))
        if numero not in marcados:
            marcados.add(numero)
            print(f"Número selecionado: {numero}")
            return numero

# Gerar a cartela de bingo 25x25
tamanho_cartela = 25
cartela = gerar_cartela_bingo(tamanho_cartela)

# Conjunto para armazenar os números marcados
marcados = set()

# Imprimir a cartela inicial
imprimir_cartela(cartela, marcados)
print("\n")

# Selecionar um número aleatório e marcá-lo
numero_selecionado = selecionar_numero(cartela, marcados)

# Imprimir a cartela atualizada
print("\nCartela após seleção:")
imprimir_cartela(cartela, marcados)
