from funcoes import valor_do_desconto
from funcoes import reducao_em_minutos


preco = float(input("digite o preço do produto"))
desconto = float(input("digite o valor do desconto em % "))
valor_final = preco - valor_do_desconto(preco,desconto)

print("um valor de %5.2f%% em uma mecadoria de %7.2f%%"% (desconto, preco))
print("vale R$ %7.2f%%"% valor_do_desconto(preco,desconto))
print("o valor final do produto e", valor_final)

cigarros_por_dia = float(input("quantidade de cigarros por dia "))
anos_fumando = float(input("quantidade de anos fumando "))

reducao_em_dias = reducao_em_minutos(cigarros_por_dia, anos_fumando) / (20*60)
print ("redução do tempo de vida %8.2f dias" % reducao_em_dias)