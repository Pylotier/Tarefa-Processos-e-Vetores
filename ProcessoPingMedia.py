import platform
import subprocess

def os():
    system: str = ''
    system = platform.system()

    return system

def le_processo(processo):
    vetor_processo: str = []
    linha: str = ''
    saida: str = ''

    vetor_processo = processo.split(' ')
    print(vetor_processo)
    linha = ''
    saida = subprocess.Popen(vetor_processo, stdout=subprocess.PIPE)
    linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

    while (linha != ''):
        if (os() == 'Windows'):

            if ('Mdia' in linha):
                #print(linha)
                pingMedia = linha.split(', ')
                #print(pingMedia)
                print('Tempo médio no Windows: ', pingMedia[2])
        elif (os() == 'Linux'):
            if ('avg' in linha):
                #print(linha)
                pingMedia = linha.split('/')
                #print(pingMedia)
                print('Tempo médio no Linux: ', pingMedia[4], 'ms')
            
        linha = saida.stdout.readline().decode('utf-8', errors = 'ignore')

def main():
    if (os() == "Windows"):
        print("Estou no Windows")
        processo: str = ''
        processo = 'ping -4 -n 10 www.google.com.br'
        le_processo(processo)
    elif (os() == "Linux"):
        print("Estou no Linux")
        processo: str = ''
        processo = 'ping -4 -c 10 www.google.com.br'
        le_processo(processo)

if __name__ == '__main__':
    main()
