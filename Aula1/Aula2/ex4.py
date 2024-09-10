def coletar_dados():
    # Coletar nomes e idades do usuário e os armazenar em uma lista de dicionários
    dados = []
    while True: 
        nome = input("Nome: (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair': 
            break 
        idade = input("Digite a idade: ")
        try: 
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um valor inteiro")
            continue
        
        dados.append({'nome': nome, 'idade': idade})
    return dados

def salvar_em_arquivo(dados, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo: 
        for item in dados: 
            linha = f"Nome: {item['nome']}, Idade: {item['idade']} \n"
            arquivo.write(linha)
                        
def main():
    dados = coletar_dados()
    
    if dados: 
        salvar_em_arquivo(dados, "dados_pessoas.txt")
        print("Dados salvos no arquivo 'dados_pessoas.txt'")
    else: 
        print("Nenhum dado foi coletado.")
                   
if __name__ == "__main__":
    main()
