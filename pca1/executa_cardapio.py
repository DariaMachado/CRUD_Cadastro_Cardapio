# Equipe: Dária Louise Barbosa Machado, Kelvin Willian Faccini de Souza,
# Eduardo Lucas Veiga de Souza, Sara Alessandra de Souza Tavares, Willian Tezolin Baldessin

# Sistema desenvolvido para cadastrar produtos em um Cardápio de uma Empresa do ramo de Alimentação Fit
from time import sleep
import uteis


uteis.carregar_prod()

while True:
    uteis.titulo('<<<<<<<<<<<<<<<<<<<< Vida Fit >>>>>>>>>>>>>>>>>>>>')

    print("       == MENU ==\n"
          "\n"
          "\t1 - Cadastrar Produto\n"
          "\t2 - Alterar Produto\n"
          "\t3 - Excluir Produto\n"
          "\t4 - Pesquisar Produto\n"
          "\t5 - Visualizar Cardápio\n"
          "\t6 - Sair\n")
    opcao = uteis.validar_menu()
    if opcao == 1:
        uteis.cadastrar()
    elif opcao == 2:
        uteis.alterar_prod()
    elif opcao == 3:
        uteis.excluir_prod()
    elif opcao == 4:
        uteis.pesquisar()
    elif opcao == 5:
        uteis.imprime_cardapio()
    elif opcao == 6:
        print('FINALIZANDO', end='')
        for i in range(0, 5):
            print('.', end='')
            sleep(0.3)
        print()
        break

print('\033[1;32m\n>> OBRIGADO! VOLTE SEMPRE! << \033[m')

