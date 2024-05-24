from scr.view.MenuCategoriasView import menu_categorias_view


def escolhe_tipo_manifestacao():
    tipos = ["Reclamação", "Elogio", "Sugestão"]
    while True:

        try:
            menu_categorias_view()
            categoria = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.\n")
            continue

        if categoria == 1:
            return tipos[0]
        elif categoria == 2:
            return tipos[1]
        elif categoria == 3:
            return tipos[2]
        else:
            print("Opção inválida. Tente novamente!")