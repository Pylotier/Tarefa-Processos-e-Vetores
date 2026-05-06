# 2. Criar e coletar um vetor [100] inteiro e exibir:
# a. O maior e o menor valor;
# b. A média dos valores.

def main():
    vetor: list[int] = [0] * 100
    maiorNumero: int = 0
    menorNumero: int = 0
    media: float = 0
    soma: int = 0

    for i in range (0, 100):
        vetor[i] = int(input("Digite um número: "))
        if (i == 0):
            maiorNumero = vetor[i]
            menorNumero = vetor[i]
        else:
            if (vetor[i] > maiorNumero):
                maiorNumero = vetor[i]
            elif (vetor[i] < menorNumero):
                menorNumero = vetor[i]
        soma += vetor[i]
        
    media = soma / 100
    print("Maior número: ", maiorNumero, "/// Menor número: ", menorNumero)
    print("Média dos valors: ",media)

if __name__ == '__main__':
    main()