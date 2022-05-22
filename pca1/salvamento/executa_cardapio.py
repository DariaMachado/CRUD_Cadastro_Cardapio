# Equipe: Dária Louise Barbosa Machado, Kelvin Willian Faccini de Souza,
# Eduardo Lucas Veiga de Souza, Sara Alessandra de Souza Tavares, Willian Tezolin Baldessin

# Sistema desenvolvido para cadastrar produtos em um Cardápio de uma Empresa do ramo de Alimentação Fit

def titulo(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


def validar_menu():
    while True:
        escolha = leiaInt('Escolha uma opcao do menu: ')
        if escolha in range(1, 6):
            return escolha
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! Digite um número inteiro váldo. \033[m')
        if ok:
            break
    return valor


def cadastrar():
    dados = dict()
    dados['nome'] = str(input('Insira o nome do produto: ').strip())
    dados['porcao'] = leiaInt('Insira a quantidade de cada porção: (g/ml) ')
    dados['preco'] = float(input('Insira o preço do produto: '))
    print('>> CATEGORIAS <<')
    print("\t1) Low Carb\n"
          "\t2) Sobremesas\n"
          "\t3) Bebidas\n")
    while True:
        cat = leiaInt('Em qual categoria deseja cadastrar o produto? Digite a opcao: ')
        if cat in range(1, 4):
            print('PRODUTO CADASTRADO COM SUCESSO!')
            break
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')
    if cat == 1:
        low_carb.append(dados.copy())
    elif cat == 2:
        sobremesas.append(dados.copy())
    elif cat == 3:
        bebidas.append(dados.copy())
    dados.clear()


def carregar_prod():
    dados = dict()
    dados['nome'] = 'Escondidinho de Abóbora com Frango'
    dados['porcao'] = 400
    dados['preco'] = 30.00
    low_carb.append(dados.copy())
    dados['nome'] = 'Lasanha de Abobrinha com Frango'
    dados['porcao'] = 400
    dados['preco'] = 28.50
    low_carb.append(dados.copy())
    dados['nome'] = 'Sorvete de Banana'
    dados['porcao'] = 150
    dados['preco'] = 10.90
    sobremesas.append(dados.copy())
    dados['nome'] = 'Brownie Fitness'
    dados['porcao'] = 250
    dados['preco'] = 15.90
    sobremesas.append(dados.copy())
    dados['nome'] = 'Smoothie Banana e Aveia'
    dados['porcao'] = 300
    dados['preco'] = 14.90
    bebidas.append(dados.copy())


def imprime_cardapio():
    titulo('############# CARDÁPIO #############')
    print(f'{"Cod.":<5}{" Produto":<35}{"Valor":>10}{" Porção(g/ml)":>8}')
    imprime_listas(low_carb)
    imprime_listas(sobremesas)
    imprime_listas(bebidas)
    print('=' * 40)


def imprime_listas(lista):
    if lista == low_carb:
        print('\n>>>  LOW CARB:')
    elif lista == sobremesas:
        print('\n>>>  SOBREMESAS:')
    elif lista == bebidas:
        print('\n>>>  BEBIDAS:')

    for i, c in enumerate(lista):
        print(f'{i:<5}{c["nome"]:<35}{c["preco"]:>10.2f}{c["porcao"]:>8}')


def alterar_prod():
    imprime_cardapio()
    print('-' * 40)
    print('Escolha a categoria a qual pertence o produto que deseja alterar:\n'
          '\t 1 - LOW CARB\n'
          '\t 2 - SOBREMESAS\n'
          '\t 3 - BEBIDAS')
    while True:
        escolha = leiaInt('\nDigite a opção: ')
        if escolha in range(1, 4):
            break
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')
    if escolha == 1:
        alterar_listas(low_carb)
    elif escolha == 2:
        alterar_listas(sobremesas)
    elif escolha == 3:
        alterar_listas(bebidas)
    print('PRODUTO ALTERADO COM SUCESSO!')


def alterar_listas(lista):
    while True:
        cod = leiaInt('\nAgora digite o codigo do produto que pretende alterar: ')
        if 0 <= cod < len(lista):
            break
        print('\033[0;31mERRO! O código não existe! Digite novamente! \033[m')

    print("Qual o campo deseja alterar?\n"
          "\t1 - Nome\n"
          "\t2 - Porção\n"
          "\t3 - Preço")
    while True:
        escolha = leiaInt('Digite a opção: ')
        if escolha in range(1, 4):
            break
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')
    if escolha == 1:
        nome = str(input('Digite o novo nome: '))
        lista[cod]['nome'] = nome
    elif escolha == 2:
        porcao = int(input('Digite o novo valor: '))
        lista[cod]['porcao'] = porcao
    elif escolha == 3:
        valor = float(input('Digite o novo preço: '))
        lista[cod]['preco'] = valor


def excluir_prod():
    imprime_cardapio()
    print('-' * 40)
    print('Escolha a categoria a qual pertence o produto que deseja deletar:\n'
          '\t 1 - LOW CARB\n'
          '\t 2 - SOBREMESAS\n'
          '\t 3 - BEBIDAS')
    while True:
        escolha = leiaInt('\nDigite a opção: ')
        if escolha in range(1, 4):
            break
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')
    if escolha == 1:
        excluir_item_lista(low_carb)
    elif escolha == 2:
        excluir_item_lista(sobremesas)
    elif escolha == 3:
        excluir_item_lista(bebidas)
    print('PRODUTO DELETADO COM SUCESSO!')


def excluir_item_lista(lista):
    while True:
        cod = leiaInt('\nAgora digite o codigo do produto que pretende deletar: ')
        if 0 <= cod < len(lista):
            break
        print('\033[0;31mERRO! O código não existe! Digite novamente! \033[m')
    lista.pop(cod)


# Programa Principal
low_carb = list()
bebidas = list()
sobremesas = list()

carregar_prod()

while True:
    titulo('<< Cardápio Fit >>')

    print("       == MENU ==\n"
          "\n"
          "\t1 - Cadastrar Produto\n"
          "\t2 - Alterar Produto\n"
          "\t3 - Excluir Produto\n"
          "\t4 - Visualizar Cardápio\n"
          "\t5 - Sair\n")
    opcao = validar_menu()
    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        alterar_prod()
    elif opcao == 3:
        excluir_prod()
    elif opcao == 4:
        imprime_cardapio()
    elif opcao == 5:
        print('FINALIZANDO...')
        break

print('\n>> OBRIGADO! VOLTE SEMPRE! <<')
