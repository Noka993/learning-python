import asyncio

async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay)
    print("Data fetched")
    return {"data": "Some data"}

async def main():
    print("Start of main coroutine")
    task = fetch_data(2)
    print("End of main coroutine")
    
    # task doesn't run yet. It has to be awaited
    result = await task
    print(f"Received result: {result}")

asyncio.run(main())