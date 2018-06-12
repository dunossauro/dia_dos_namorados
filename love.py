from os import system, name
from random import choice
from time import sleep
from click import command, option, echo
from colorama import init, Back
from pyfiglet import Figlet

init(autoreset=True)

back = list(vars(Back).values())


def clear():
    if name == 'posix':
        system('clear')
    else:
        system('cls')


def full_style(love_string: str) -> str:
    f = Figlet(font='doom')
    selected_back = choice(back)
    return f'{selected_back}{f.renderText(love_string)}'


@command()
@option('--name', prompt='Nome do seu amor')
def love(name):
    loved = 'Eu te amo ' + name
    while True:
        try:
            echo(full_style(loved))
            clear()
            sleep(0.3)
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    love()
