import asyncio
from nats.aio.client import Client as NATS
from nats.js.api import KeyValueConfig

async def main():
    print("\n Please ensure your NATS cluster is running using: `docker-compose up -d`\n")

    # Wait for user confirmation
    input("Press ENTER once your NATS cluster is up and running...")

    nc = NATS()

    try:
        await nc.connect(servers=[
            "nats://admin:natsdemo@localhost:4222",
            "nats://admin:natsdemo@localhost:4223",
            "nats://admin:natsdemo@localhost:4224"
        ])
        print(" Connected to NATS cluster.")
    except Exception as e:
        print(f" Failed to connect to NATS: {e}")
        return  # Exit early if connection fails

    # Get a JetStream context
    try:
        js = nc.jetstream()
        print(" JetStream initialized.")
    except Exception as e:
        print(f" Failed to initialize JetStream: {e}")
        return

    # Create a Key-Value bucket
    try:
        await js.create_key_value(KeyValueConfig(bucket="my_demo_bucket", replicas=3))
        print(" Key-Value bucket created: my_demo_bucket")
    except Exception as e:
        print(f" Bucket already exists or error occurred: {e}")

    # Put a value
    kv = await js.key_value("my_demo_bucket")
    await kv.put("my_key", b"My Value")
    print(" Value stored successfully.")

    # Get the value
    entry = await kv.get("my_key")
    print(f" Retrieved value: {entry.value.decode()}")

    # Prompt user to stop a server
    input("\n Now, stop one of the NATS servers manually (e.g., `docker stop <container_id>`) and press ENTER to continue...")

    # Try retrieving the value again
    try:
        entry = await kv.get("my_key")
        print(f" Retrieved value after stopping a server: {entry.value.decode()}")
    except Exception as e:
        print(f" Error retrieving value after stopping a server: {e}")

    # Close connection
    await nc.close()
    print(" Connection closed.")

if __name__ == "__main__":
    asyncio.run(main())
