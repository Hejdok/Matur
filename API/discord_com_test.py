import httpx
import asyncio

async def test_communication():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://discord.com/api/v10/gateway")
            print("Api connection works, {response.code_status}")

    except Exception as e:
        print((f"Discord blocked, {e}"))


asyncio.run(test_communication())
