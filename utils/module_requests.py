from typing import List
from utils.settings import TOKEN
import asyncio
import aiohttp
import json


class Requests:
    """
    Класс представляющий асинхронные запросы к внешнему API
    """

    def __init__(self, nums: List[str], url: str) -> None:
        """
        :param nums: список с эдпоинтами
        :param url: url сайта кинопоиск
        """
        self.__nums = nums
        self.__url = url

    async def _get_info(self, num: str, session):
        """
        Метод для непосредственного запроса к внешнему API сайта кинопоиск
        :param num: эндпоинт url
        :param session: сессия пользователя
        :return: ответ запроса в формате json
        """
        async with session.get(url=f"{self.__url}{num}", headers=TOKEN) as response:
            return await response.json()

    async def main(self) -> None:
        """
        Функция для складывания задач и их асинхронного запуска
        """
        async with aiohttp.ClientSession() as session:
            tasks: List[asyncio.Task] = []
            for endpoint in self.__nums:
                task = asyncio.create_task(self._get_info(num=endpoint, session=session))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            for index, response in enumerate(responses):
                print(f"{index + 1} результат: {json.dumps(response, indent=4)}")
