from colorama import Fore, Style, init

# Inicializa o colorama
init()

def classificar_reservatorio(percentual):
    """
    Classifica o nível do reservatório com base na porcentagem informada.
    """
    if percentual < 20:
        return Fore.RED, "Nível Crítico (Muito Baixo)"
    elif percentual < 40:
        return Fore.YELLOW, "Nível Baixo"
    elif percentual < 60:
        return Fore.GREEN, "Nível Moderado"
    elif percentual < 80:
        return Fore.CYAN, "Nível Alto"
    else:
        return Fore.BLUE, "Nível Muito Alto (Alerta)"

def executar_sistema():
    print(f"{Style.BRIGHT}--- SISTEMA DE ENTRADA DE DADOS: RESERVATÓRIO ---{Style.RESET_ALL}")
    
    try:
        # Entrada de dados do usuário
        valor = float(input("Digite a porcentagem atual da água (0 a 100): "))

        if 0 <= valor <= 100:
            cor, situacao = classificar_reservatorio(valor)
            
            # Exibição do resultado
            print("\n" + "="*40)
            print(f"Status para {valor}% de preenchimento:")
            print(f"SITUAÇÃO: {cor}{situacao}{Style.RESET_ALL}")
            print("="*40)
        else:
            print(f"\n{Fore.RED}Erro: Por favor, digite um valor entre 0 e 100.{Style.RESET_ALL}")

    except ValueError:
        print(f"\n{Fore.RED}Erro: Entrada inválida! Digite apenas números.{Style.RESET_ALL}")

    print(f"\n{Style.DIM}Estilo do terminal restaurado. Encerrando...{Style.RESET_ALL}")

if __name__ == "__main__":
    executar_sistema()