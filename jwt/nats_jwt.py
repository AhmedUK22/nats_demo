import asyncio
import os

import nats

async def main():
    nc = await nats.connect(user_credentials=os.path.abspath("anglesey_client_demo.cred"))

    async def subscribe_handler(msg):
        print(f"Received message: {msg.data.decode()}")

    await nc.subscribe("my_subject", cb=subscribe_handler)

    await nc.publish("my_subject", b"Hello, NATS!")

    await nc.drain()

if __name__ == '__main__':
    asyncio.run(main())
