def main():
    vetor2 = []
    
    for i in range(10):
        vetor2.append(int(input("Digite o elemento %d: " % i)))
    
    maior = vetor2[0]
    menor = vetor2[0]
    
    for i in range(len(vetor2)):
        if vetor2[i] > maior:
            maior = vetor2[i]
        if vetor2[i] < menor:
            menor = vetor2[i]
            
    print("Maior elemento: %d" % maior)
    print("Menor elemento: %d" % menor)
    
 #somar vetores de forma modularizada    

if __name__ == "__main__":
    main()