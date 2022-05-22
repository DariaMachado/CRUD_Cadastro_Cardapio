low_carb = list()
bebidas = list()
sobremesas = list()
import unidecode  # Baixar essa biblioteca para desconsiderar os acentos em strings


def titulo(msg):
    """
    Configura um título conforme o tamanho da string que recebe
    :param msg: Mensagem do título
    :return: Sem retorno. Imprime o título configurado
    """
    tam = len(msg) + 4
    print('\033[1;33m', end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print('\033[m', end='')


def validar_menu():
    """
    Valida se a opcao escolhida pelo usuário está entre as existentes no menu do sistema.
    :return: Retorna a opcao feita pelo usuário caso seja válida.
    """
    while True:
        escolha = leiaInt('Escolha uma opcao do menu: ')
        if escolha in range(1, 7):
            return escolha
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')


def leiaInt(msg):
    """
    Verifica se opção digitada pelo usuário é um número inteiro
    :param msg: Opção digitada pelo usuário
    :return: Retorna o valor se este for válido
    """
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
    """
    Cadastra um produto no cardápio.
    :return: Sem retorno. Apenas imprime uma mensagem ao final do cadastro.
    """
    dados = dict()
    print('-' * 30)
    print('\033[4;29mCADASTRO:\033[m')
    dados['nome'] = unidecode.unidecode(str(input('Insira o nome do produto: ').strip().title()))
    dados['porcao'] = leiaInt('Insira a quantidade de cada porção: (g/ml) ')
    dados['preco'] = float(input('Insira o preço do produto: '))
    cat = escolha_cat('cadastrar')
    if cat == 1:
        low_carb.append(dados.copy())
    elif cat == 2:
        sobremesas.append(dados.copy())
    elif cat == 3:
        bebidas.append(dados.copy())
    print('\033[0;34mPRODUTO CADASTRADO COM SUCESSO!\033[m')
    print('-' * 30)
    dados.clear()


def escolha_cat(opc):
    """
    Valida se a opção escolhida pelo usuário está entre as categorias existentes no menu.
    :param opc: Opção digitada pelo usuário
    :return: Retorna a opcao feita pelo usuário caso seja válida.
    """
    print('-' * 30)
    print(f'Em qual categoria deseja {opc} o produto?\n'
          '\t\033[0;32m 1 - Low Carb\n'
          '\t 2 - Sobremesas\n'
          '\t 3 - Bebidas \033[m')
    while True:
        escolha = leiaInt('\nDigite a opção: ')
        if escolha in range(1, 4):
            break
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')
    print('-' * 30)
    return escolha


def carregar_prod():
    """
    Carrega previamente itens no cardápio com a finalidade de simular um sistema funcional com acesso ao banco de dados
    :return: Sem retorno
    """
    dados = dict()
    dados['nome'] = 'Escondidinho De Abobora Com Frango'
    dados['porcao'] = 400
    dados['preco'] = 30.00
    low_carb.append(dados.copy())
    dados['nome'] = 'Lasanha De Abobrinha Com Frango'
    dados['porcao'] = 400
    dados['preco'] = 28.50
    low_carb.append(dados.copy())
    dados['nome'] = 'Sorvete De Banana'
    dados['porcao'] = 150
    dados['preco'] = 10.90
    sobremesas.append(dados.copy())
    dados['nome'] = 'Brownie Fitness'
    dados['porcao'] = 250
    dados['preco'] = 15.90
    sobremesas.append(dados.copy())
    dados['nome'] = 'Smoothie Banana E Aveia'
    dados['porcao'] = 300
    dados['preco'] = 14.90
    bebidas.append(dados.copy())


def imprime_cardapio():
    """
    Imprime o cardápio na tela.
    :return: Sem retorno.
    """
    titulo('>>>>>>>>>>>>>>>> CARDÁPIO <<<<<<<<<<<<<<<')
    print('\033[7;40m', end='')
    print(f'{"Cod.":<5}{" Produto":<35}{"Valor":>10}{" Porção(g/ml)":>8}')
    imprime_listas(low_carb)
    imprime_listas(sobremesas)
    imprime_listas(bebidas)
    print('=' * 30)
    print('\033[m', end='')


def imprime_listas(lista):
    """
    Imprime uma determinada lista de categorias do cardápio.
    :param lista: lista determinada pelo usuário.
    :return: Sem retorno.
    """
    print('\033[7;40m', end='')
    if lista == low_carb:
        print('\n>>>  LOW CARB:')
    elif lista == sobremesas:
        print('\n>>>  SOBREMESAS:')
    elif lista == bebidas:
        print('\n>>>  BEBIDAS:')

    for i, c in enumerate(lista):
        print(f'{i:<5}{c["nome"]:<35}{c["preco"]:>10.2f}{c["porcao"]:>8}')
    print('\033[m', end='')


def alterar_prod():
    """
    Altera um produto existente no cardápio com base em uma determinada categoria escolhida pelo usuário.
    :return: Sem retorno. Imprime uma mensagem na tela ao final do processo de alteração.
    """
    escolha = escolha_cat('alterar')
    print(f'\033[7;40m{"Cod.":<5}{" Produto":<35}{"Valor":>10}{" Porção(g/ml)":>8}\033[m', end='')
    if escolha == 1:
        imprime_listas(low_carb)
        alterar_listas(low_carb)
    elif escolha == 2:
        imprime_listas(sobremesas)
        alterar_listas(sobremesas)
    elif escolha == 3:
        imprime_listas(bebidas)
        alterar_listas(bebidas)
    print('-' * 30)
    print('\033[0;34mPRODUTO ALTERADO COM SUCESSO! \033[m')
    print('-' * 30)


def alterar_listas(lista):
    """
    Altera um produto existente em uma categoria. Usuário deve escolher o campo de alteração.
    :return: Sem retorno.
    """
    print('-' * 30)
    while True:
        cod = leiaInt('Agora digite o codigo do produto que pretende alterar: ')
        if 0 <= cod < len(lista):
            break
        print('\033[0;31mERRO! O código não existe! Digite novamente! \033[m')

    print("Qual o campo deseja alterar?\n"
          "\t\033[0;32m1 - Nome\n"
          "\t2 - Porção\n"
          "\t3 - Preço \033[m")
    while True:
        escolha = leiaInt('\nDigite a opção: ')
        if escolha in range(1, 4):
            break
        print('\033[0;31mERRO! Escolha uma opção válida! \033[m')
    if escolha == 1:
        nome = unidecode.unidecode(str(input('Digite o novo nome: ')).strip().title())
        lista[cod]['nome'] = nome
    elif escolha == 2:
        porcao = int(input('Digite o novo valor: '))
        lista[cod]['porcao'] = porcao
    elif escolha == 3:
        valor = float(input('Digite o novo preço: '))
        lista[cod]['preco'] = valor


def excluir_prod():
    """
    Exclui um produto do cardápio com base em uma determinada categoria.
    :return: Sem retorno. Imprime uma mensagem na tela ao final do processo de exclusão.
    """
    escolha = escolha_cat('excluir')
    print(f'\033[7;40m{"Cod.":<5}{" Produto":<35}{"Valor":>10}{" Porção(g/ml)":>8}\033[m', end='')
    if escolha == 1:
        imprime_listas(low_carb)
        excluir_item_lista(low_carb)
    elif escolha == 2:
        imprime_listas(sobremesas)
        excluir_item_lista(sobremesas)
    elif escolha == 3:
        imprime_listas(bebidas)
        excluir_item_lista(bebidas)
    print('\033[0;34mPRODUTO DELETADO COM SUCESSO!\033[m')
    print('-' * 30)


def excluir_item_lista(lista):
    """
    Deleta um produto existente em uma categoria e verifica se o codigo do produto escolhido é válido.
    :return: Sem retorno.
    """
    while True:
        cod = leiaInt('\nAgora digite o codigo do produto que pretende deletar: ')
        if 0 <= cod < len(lista):
            break
        print('\033[0;31mERRO! O código não existe! Digite novamente! \033[m')
    lista.pop(cod)


def pesquisar():
    """
    Pesquisa um produto a partir do seu nome na lista de categorias. Caso não exista no cadastro,
    dá ao usuário a opção de cadastrá-lo.
    :return: Sem retorno. Imprime os dados do produto caso exista no cadastro.
    """
    print('-' * 30)
    prod = unidecode.unidecode(str(input('Digite o nome do produto: ').strip().title()))
    print('=> RESULTADO: ')
    result = False
    for c in low_carb:
        if c['nome'] == prod:
            print(f'Nome: {c["nome"]}')
            print(f'Porção g/ml: {c["porcao"]}')
            print(f'Preço: {c["preco"]:.2f}')
            print(f'Categoria: Low Carb')
            result = True
    for c in sobremesas:
        if c['nome'] == prod:
            print(f'Nome: {c["nome"]}')
            print(f'Porção g/ml: {c["porcao"]}')
            print(f'Preço: {c["preco"]:.2f}')
            print(f'Categoria: Sobremesas')
            result = True
    for c in bebidas:
        if c['nome'] == prod:
            print(f'Nome: {c["nome"]}')
            print(f'Porção g/ml: {c["porcao"]}')
            print(f'Preço: {c["preco"]:.2f}')
            print(f'Categoria: Bebidas')
            result = True
    if not result:
        print('\033[0;31mPRODUTO NÃO ENCONTRADO!\033[m')
        print('-' * 30)
        while True:
            opcao = str(input('Deseja cadastrar? [S/N] ').strip().upper()[0])
            if opcao in 'SN':
                break
            print('\033[0;31mERRO! Digite apenas S ou N! \033[m')
        if opcao == 'S':
            cadastrar()
