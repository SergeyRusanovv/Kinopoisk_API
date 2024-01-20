from typing import List
from utils.settings import TOKEN
import asyncio
import aiohttp


class Requests:
    """
    Класс представляющий асинхронные запросы к внешнему API
    """
    __url = "https://api.kinopoisk.dev/v1.4/movie/"

    def __init__(self, nums: List[str]) -> None:
        """
        :param nums: список с эдпоинтами
        """
        self.nums = nums

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
            for endpoint in self.nums:
                task = asyncio.create_task(self._get_info(num=endpoint, session=session))
                tasks.append(task)

            responses = await asyncio.gather(*tasks)
            for response in responses:
                print(response)
