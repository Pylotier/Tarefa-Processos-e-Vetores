# 1. Criar e coletar um vetor [50] inteiro. Calcular e exibir:
# a. A média dos valores entre 10 e 200;
# b. A soma dos números ímpares.

def main():

    vetorNumeros: list[int] = [0] * 50
    somaMedia: int = 0
    somaImpares:int = 0
    media: float = 0.0

    for i in range (0, 50):
        vetorNumeros[i] = int(input("Digite um número: "))
        if (vetorNumeros[i] % 2 != 0):
            somaImpares += vetorNumeros[i]

        if (vetorNumeros[i] >= 10 and vetorNumeros[i] <= 200):
            somaMedia += vetorNumeros[i]

    media = somaMedia / 50

    print("Média dos 100 números: ", media)
    print("A soma dos impares: ", somaImpares)

if __name__ == "__main__":
    main()