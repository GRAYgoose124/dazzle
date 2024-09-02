import asyncio
import json
import os
import zmq
import logging

from dizzy.daemon.client.asy import SimpleAsyncClient
from dizzy.utils import load_dizzy_proto_class

logging.basicConfig(level=getattr(logging, os.getenv("DIZZY_LOG_LEVEL", "INFO")), filename="/app/dizzy_client.log")

DizzyProtocol = load_dizzy_proto_class()


dizzy_client = SimpleAsyncClient(
    DizzyProtocol,
    address=os.environ.get("DIZZY_COMPUTE_HOST", "localhost"),
    port=os.environ.get("DIZZY_COMPUTE_PORT", 4242),
)


def main():
    # test request
    request = DizzyProtocol.Request(
        entity="einz",
        workflow="einzy",
        task="einzyA",
        options={"test": "test"},
    )

    async def test():
        response = await dizzy_client.send_request(request.to_dict())
        print(response)

    asyncio.run(test())

if __name__ == "__main__":
    main()
    # pass
