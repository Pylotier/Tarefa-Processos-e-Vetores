import platform
import subprocess

def main():
    opcao: int = 0
    processo: str = ''
    PID: int = ''

    opcao = int(input("Digite uma das opções:\n1-Lista de Processos\n2-Matar um processo pelo PID\n3-Matar um processo pelo nome\n9-Encerrar sessão\n"))

    while (opcao != 9):
        match opcao:
            case 1: # LISTAR os processo
                if (os() == "Windows"):
                    processo = 'TASKLIST /FO TABLE'
                    processoLista(processo)
                elif (os() == "Linux"):
                    processo = 'ps -ef'
                    processoLista(processo)

            case 2: # Matar um processo com PID
                if (os() == "Windows"):
                    # TASKKILL /PID pid_do_processo
                    PID = int(input("Digite qual processo a matar: "))
                    processo = 'TASKKILL /PID '
                    matarProcessoPID(processo, str(PID))
                elif (os() == "Linux"):
                    # kill -9 pid_do_processo
                    PID = int(input("Digite qual processo a matar: "))
                    processo = 'kill -9 '
                    matarProcessoPID(processo, str(PID))
                    
            case 3: # Matar um processo com NOME
                if (os() == "Windows"):
                    # TASKKILL /IM nome_do_processo
                    NOME = input("Digite o nome do processo: ")
                    processo = 'TASKKILL /IM '
                    matarProcessoNOME(processo, NOME)
                elif (os() == "Linux"):
                    # pkill -f nome_do_processo
                    NOME = input("Digite o nome do processo: ")
                    processo = 'pkill -f '
                    matarProcessoNOME(processo, NOME)
            case 9: # ENCERRAR
                print("ENCERRAR")

        opcao = int(input("\n1-Listar\n2-Matar pelo PID\n3-Matar pelo nome\n9-Encerrar\n"))

def os():
    system: str = ''
    system = platform.system()

    return system

def processoLista(processo):
    vetor_processo: str = []
    vetor_processo = processo.split(' ')
    print(vetor_processo)
    subprocess.run(vetor_processo)

def matarProcessoPID(processo, PID):
    vetor_processo : str = []
    vetor_processo = processo.split(' ')
    vetor_processo[2] = PID

    subprocess.run(vetor_processo)

def matarProcessoNOME(processo, NOME):
    vetor_processo : str = []
    vetor_processo = processo.split(' ')
    vetor_processo[2] = NOME
    
    subprocess.run(vetor_processo)

    vetor_processo = processo.split
if __name__ == '__main__':
    main()