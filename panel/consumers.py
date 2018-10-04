from channels.generic.websocket import AsyncWebsocketConsumer
import json

from panel.gateway_api import Gateway


class PanelConsumer(AsyncWebsocketConsumer):
    async def connect(self, *args, **kwargs):
        await self.accept()

    async def disconnect(self, close_code):
        await self.close()

    async def receive(self, text_data):
        data = json.loads(text_data)

        method = data['method']
        print(data)

        if method == 'getNumbersStatus':
            api_key = data['api_key']
            gateway = Gateway(api_key)
            available_numbers = await gateway.getNumbersStatus()

            await self.send(text_data=json.dumps({
                'method': 'getNumbersStatus',
                'available_numbers': available_numbers
            }))
        if method == "registerAccounts":
            api_key = data['api_key']
            accounts_number = data['accounts_number']
            gateway = Gateway(api_key)
            available_numbers = await gateway.registerAccounts(accounts_number)
