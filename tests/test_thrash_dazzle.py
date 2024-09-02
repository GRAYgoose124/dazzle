# test that dazzle can handle a large number of requests, ensure dazzle is up.

import asyncio
import pytest

from dizzy.daemon.client.asy import SimpleAsyncClient
from dizzy.daemon.protocol import Request


class TestThrashDazzle:
    @pytest.mark.asyncio
    async def test_thrash_dazzle(self, n_clients: int = 10, n_requests: int = 100):
        clients = [SimpleAsyncClient(address="localhost", port=4242) for _ in range(n_clients)]
        requests = [Request(entity="test", workflow="test", task="testA", options={"test": "test"}) for _ in range(n_requests)]

        async def send_requests():
            while requests:
                async with asyncio.TaskGroup() as tg:
                    for client in clients:
                        tg.create_task(client.send_request(requests.pop(0).to_dict()))

        asyncio.run(send_requests())
