def valor_do_desconto(preco, desconto):
    valor = preco * desconto /100
    return valor 

def reducao_em_minutos(anos_fumando, cigarros_por_dia):
   valor_final = anos_fumando*365*cigarros_por_dia*10
   return valor_final

def soma_de_vetores(x, y, vector):
    soma = vector[x] + vector[y]
    return soma