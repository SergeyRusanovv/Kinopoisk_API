import asyncio
from typing import List

from utils.module_requests import Requests
from utils import messages


def menu():
    """
    Функция представляющая интерфейс программы
    :return: None
    """
    while True:
        choice: str = input(
            "Введите что вы хотите найти: \n1 - один или  несколько фильмов \n2 - одного или несколько актеров"
            "\nexit - выход\n"
        )
        if choice == "exit":
            print(messages.EXIT_MESSAGE)
            break

        elif choice == "1":
            num_range: str = input(
                "\nНапишите одну или несколько цифр с пробелом от 250 до 7000000"
                "для получения информации об этих фильмах: "
            )
            numbers: List[str] = num_range.split(" ")
            request_cls: Requests = Requests(nums=numbers, url="https://api.kinopoisk.dev/v1.4/movie/")
        elif choice == "2":
            num_range: str = input(
                "\nНапишите одну или несколько цифр с пробелом "
                "для получения информации об этих актеров "
            )
            numbers: List[str] = num_range.split(" ")
            request_cls: Requests = Requests(nums=numbers, url="https://api.kinopoisk.dev/v1.4/person/")

        print(messages.OUTPUT_MESSAGE)
        asyncio.run(request_cls.main())


if __name__ == "__main__":
    menu()
