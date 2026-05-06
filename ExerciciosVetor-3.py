# 3. Criar e coletar em um vetor [30] real e calcular e exibir:
# a. A média do grupo;
# b. A quantidade de notas acima do grupo;
# c. As posições dos valores abaixo da média do grupo.

def main():

    valoresVetor: list[float] = [0] * 30
    vetorAbaixaMedia: list[float] = [0] * 30
    vetorAcimaMedia: list[float] = [0] * 30
    media: float = 0.0
    somaMedia: float = 0.0
    for i in range (0, 30):
        valoresVetor[i] = float(input("Digite um valor: "))
        somaMedia += valoresVetor[i]
    media = somaMedia / 30

    for i in range (0, 30):
        if (valoresVetor[i] < media):
            vetorAbaixaMedia[i] = valoresVetor[i]
        else:
            vetorAcimaMedia[i] = valoresVetor[i]


    print ("Média dos valores: ", media)
    
    print ("Valores acima da média: ")
    for i in range (0, 30):
        if (vetorAcimaMedia[i] > media):
            print(i+1, "° aluno com: ", vetorAcimaMedia[i])

    print ("Valores abaixo da média: ")
    for i in range (0, 30):
        if (vetorAcimaMedia[i] < media):
            print(i+1, "° aluno com: ", vetorAbaixaMedia[i])

if __name__ == '__main__':
    main()