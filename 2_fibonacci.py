anterior = 0
proxima = 1 
soma = 1 

entrada = int(input("Insira um numéro e verifique se contém na sequência de Fibonacci: "))

pertence = False

for n in range(0,31):
    print(anterior)
    
    if anterior == entrada:
        pertence = True
        break
    
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
    

if pertence:
    print(f'O numéro {entrada} pertence a sequência de Finabocci')
else:
    print(f'O número {entrada} não possui a sequência de Finnabocci')
         
  
    
   
    
