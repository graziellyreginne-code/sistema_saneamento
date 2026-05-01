import time
from colorama import Fore, Style, init

# Inicializa o colorama (necessário para Windows)
init()

def exibir_alerta(nivel_indice):
    """
    Função que define a cor e a mensagem com base no nível do reservatório.
    O nível_indice deve ser de 0 a 4 (referente aos níveis 1 a 5).
    """
    
    # Lista de situações conforme o cenário proposto
    situacoes = [
        "Muito baixo (crítico)", # Nível 1
        "Baixo",                 # Nível 2
        "Médio",                 # Nível 3
        "Alto",                  # Nível 4
        "Muito alto (alerta)"    # Nível 5
    ]
    
    # Dicionário mapeando o índice do nível para a cor correspondente
    cores = {
        0: Fore.RED,
        1: Fore.YELLOW,
        2: Fore.GREEN,
        3: Fore.CYAN,
        4: Fore.BLUE
    }

    # Seleção da cor e mensagem
    cor_selecionada = cores.get(nivel_indice, Fore.WHITE)
    mensagem = situacoes[nivel_indice]
    
    # Exibição formatada
    print(f"Monitoramento: Nível {nivel_indice + 1} -> {cor_selecionada}{mensagem}{Style.RESET_ALL}")

def simular_monitoramento():
    """
    Simula a leitura do reservatório percorrendo todos os níveis da lista.
    """
    print("--- INICIANDO SISTEMA DE MONITORAMENTO ETEC ---")
    
    # Simulando a varredura de todos os níveis (1 a 5)
    for i in range(5):
        exibir_alerta(i)
        time.sleep(1)  # Pausa de 1 segundo para simular tempo real
        
    print("-----------------------------------------------")
    print("Monitoramento concluído. Estilo do terminal restaurado.")

# Execução do Programa
if __name__ == "__main__":
    simular_monitoramento()