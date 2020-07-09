'''
    Qual é o tipo do triângulo?
    Eduardo Seige Ianaguivara
'''

print("Programa que determina o tipo do triângulo")
ladoA = input("Insira o tamanho do primeiro lado do triângulo.: ") # Inserção do primeiro lado do triângulo
ladoB = input("Insira o tamanho do segundo lado do triângulo.: ") # Inserção do segundo lado do triângulo
ladoC = input("Insira o tamanho do terceiro lado do triângulo.: ") # Inserção do terceiro lado do triângulo
A = 0.0 # Variável que armazenará o valor da primeira entrada de dados
B = 0.0 # Variável que armazenará o valor da segunda entrada de dados
C = 0.0 # Variável que armazenará o valor do terceiro entrada de dados

A = float(ladoA) # Atribuição do primeiro lado para a variável A
B = float(ladoB) # Atribuição do segundo lado para a variável B
C = float(ladoC) # Atribuição do terceiro lado para a variável C

'''
    No bloco de condição, podemos colocar os conectivos lógico AND, OR e NOT
    No primeiro teste, testamos igualdade de lados entre os 3 lados
    No segundo bloco condicional, testamos a segunda opção condicional onde.:
        Com dois lados iguais, testamos se tem um diferente.
    No final, o bloco diferente dos anteriores.
    Observação.:
        Dentro de um elif, podemos possuír IF's...
'''

if A == B and A == C and B == C:
    print("Triângulo equilatero") # Lados iguais

elif A == B or A == C:
    if A != B or A != C:
        print("Triângulo Isósceles") # Dois lados iguais e 1 lado diferente

else:
    print("Triângulo escaleno") # Os três lados são diferentes

