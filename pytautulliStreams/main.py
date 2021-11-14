#!/bin/python3
import asyncio
import json

from pytautulli import PyTautulli, PyTautulliHostConfiguration

IP = ""
TOKEN = ""


async def main():
    host_configuration = PyTautulliHostConfiguration(ipaddress=IP, api_token=TOKEN)
    async with PyTautulli(host_configuration=host_configuration) as client:
        z = str(await client.async_command("get_activity"))
        z = z.split("sessions", 1)[0][:-3]
        for i in range(z.count('{')):
            z += "}"
        z = z.replace("'", '"').replace("True", '"True"').replace("False", '"False"').replace("None", '"None"')

        zd = json.loads(z)
        if 'response' in zd:
            if 'data' in zd['response']:
                if 'stream_count' in zd['response']['data']:
                    print(zd['response']['data']['stream_count'])

asyncio.get_event_loop().run_until_complete(main())