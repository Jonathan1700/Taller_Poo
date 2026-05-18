from data.bloques import BLOQUES
from controllers.menu_controller import Menu


def main():
    menu = Menu(BLOQUES)
    menu.mostrar_principal()


if __name__ == "__main__":
    main()
