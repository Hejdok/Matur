import asyncio

async def make_coffee():
    print("Coffee starting...")
    await asyncio.sleep(3)
    print("Coffee is ready!")
    return "coffew"


async def make_yoghurt():
    print("Getting yoghurt...")
    await asyncio.sleep(2)
    print("Yoghurt at the table")
    return "yoghew"

async def make_breakfast():
    coffee, yoghurt = await asyncio.gather(
        make_coffee(),
        make_yoghurt()
    )
    print(f"Braekfast is ready: {coffee}, {yoghurt}")

asyncio.run(make_breakfast())