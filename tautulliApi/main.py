#!/bin/python3
import asyncio
from pytautulli import PyTautulli, PyTautulliHostConfiguration

IP = ""
TOKEN = ""


async def async_example():
    host_configuration = PyTautulliHostConfiguration(ipaddress=IP, api_token=TOKEN)
    async with PyTautulli(host_configuration=host_configuration) as client:
        print(await client.async_command("get_activity"))


asyncio.get_event_loop().run_until_complete(async_example())

