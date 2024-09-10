def main(): 
    vetor_a = []
    vetor_b = []
    vetor_c = []

    for i in range(10):
        vetor_a.append(int(input("digite o elemento %d do vetor A: " % i)))
        vetor_b.append(int(input("digite o elemento %d do vetor B: " % i)))
        
    for i in range(10):
        vetor_c.append(vetor_a[i] + vetor_b[i])
            
    print("vetor C: ")
        
    for i in range(10):
        print(vetor_c[i])
                
if __name__ == "__main__":
    main()
    
