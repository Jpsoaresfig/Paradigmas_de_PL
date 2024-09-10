
from funcoes import soma_de_vetores







def main():
        


        
        
        

        vetor = [0] * 8 

        for i in range (8):
                vetor[i] = int(input("Digite o valor da posição {}".format(i)))
        
        
        x = int(input("digite o valor de x: "))
        y = int(input("digite o valor de x: "))  
        
        
        
        print("a soma dos valores nas posições x e y é {}. " % soma_de_vetores (x,y,) )
        
        if __name__ == "__main__":
                main()