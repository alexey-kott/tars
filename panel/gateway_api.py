import json
import asyncio

from aiohttp import ClientSession


class Gateway():
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = 'http://sms-activate.ru/stubs/handler_api.php'

    async def sendRequest(self, params):
        async with ClientSession() as session:
            async with session.get(self.api_url, params=params) as response:
                return await response.text()

    async def getNumbersStatus(self):
        params = {
            'api_key': self.api_key,
            'action': 'getNumbersStatus',
            'country': 0  # Россия
        }
        text_response = await self.sendRequest(params)
        data = json.loads(text_response)
        print(data)

        return data['tg_0']  # нас интересует только Telegram

    async def getNumber(self):
        params = {
            'api_key': self.api_key,
            'action': 'getNumber',
            'service': 'tg',
            'country': 0
        }

        text_response = await self.sendRequest(params)  # ACCESS_NUMBER:81104624:79658794570
        service_message = text_response.split(':')[0]

        if service_message == 'ACCESS_NUMBER':
            operation_id = text_response.split(':')[1]
            phone_number = text_response.split(':')[2]

            return operation_id, phone_number

    async def getStatus(self, operation_id):
        params = {
            'api_key': self.api_key,
            'action': 'getStatus',
            'id': operation_id
        }

        text_response = await self.sendRequest(params)
        service_message = text_response.split(':')[0]

        if service_message == 'STATUS_OK':
            code = text_response.split(':')[1]



    async def registerAccounts(self, accounts_number):
        tasks = [self.getNumber() for i in range(accounts_number)]

        results = await asyncio.gather(*tasks)

        new_accounts = []

        for operation_id, phone in results:
            pass

