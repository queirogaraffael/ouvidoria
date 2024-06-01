from src.view.MenuPrincipalView import menu_view
from src.utils.EscolheTipoManifestacao import escolhe_tipo_manifestacao
from src.service.ManifestacaoDAO import *


def ouvidoria_controller():
    while True:
        try:
            menu_view()
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.\n")
            continue

        if opcao == 1:
            lista_manifestacoes()
        elif opcao == 2:
            lista_manifestacao_por_tipo()
        elif opcao == 3:
            cria_uma_manifestacao()
        elif opcao == 4:
            exibe_numero_manifestacoes()
        elif opcao == 5:
            pesquisa_manifestacao_por_codigo()
        elif opcao == 6:
            exclui_manifestacao()
        elif opcao == 7:
            exit()
        else:
            print("Opção inválida")


def lista_manifestacoes():
    numero_manifestacoes = retorna_tamanho_tabela_manifestacoes()
    if numero_manifestacoes == 0:
        print("Não existe manifestações cadastradas")
    else:
        manifestacoes = retorna_manifestcoes()
        exibe_manifestacaos(manifestacoes)


def lista_manifestacao_por_tipo():
    tipo = escolhe_tipo_manifestacao()
    numero_manifestacoes_por_tipo = retorna_tamanho_tabela_manifestacoes_por_tipo(tipo)

    if numero_manifestacoes_por_tipo == 0:
        print(f"Não existe manifestações cadastradas do tipo: {tipo}")
    else:
        manifestacao = retorna_manifestacoes_por_tipo(tipo)
        exibe_manifestacaos(manifestacao)


def cria_uma_manifestacao():
    descricao = input("Digite a mensagem da manifestação: ")
    tipo = escolhe_tipo_manifestacao()
    manifestacao = (descricao, tipo)
    cria_manifestacao(manifestacao)


def exibe_numero_manifestacoes():
    numero_manifestacoes = retorna_tamanho_tabela_manifestacoes()
    print(f"Número de manifestações: {numero_manifestacoes}\n")


def pesquisa_manifestacao_por_codigo():
    # fazer tratamento
    codigo = int(input("Digite o código da manifestação: "))
    manifestacao = retorna_manifestacao_por_codigo(codigo)

    if len(manifestacao) == 0:
        print("Manifestação com esse código não existe. Tente outro!")
    else:
        exibe_manifestacaos(manifestacao)


def exclui_manifestacao():
    codigo = int(input("Digite o código da manifestação que deseja excluir: "))
    remove_manifestacao(codigo)


def exibe_manifestacaos(manifestacoes):
    print("\nManifestações: \n")
    for manifestacao in manifestacoes:
        print(f"Código: {manifestacao[0]}")
        print(f"Descrição: {manifestacao[1]}")
        print(f"Tipo: {manifestacao[2]}\n")
