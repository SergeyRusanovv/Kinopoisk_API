import asyncio
from utils.module_requests import Requests
from utils import messages


def menu():
    """
    Функция представляющая интерфейс программы
    :return: None
    """
    while True:
        choice = input(
            "\nНапишите одну или несколько цифр с пробелом "
            "для получения информации об этих фильмах (exit для выхода): "
        )
        if choice == "exit":
            print(messages.EXIT_MESSAGE)
            break

        numbers = choice.split(" ")
        request_cls = Requests(nums=numbers)
        print(messages.OUTPUT_MESSAGE)
        asyncio.run(request_cls.main())


if __name__ == "__main__":
    menu()
