import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"data": f"Sample data from coroutine {id}", "id": id}

async def main():
    # task1 = asyncio.create_task(fetch_data(1, 2))
    # task2 = asyncio.create_task(fetch_data(2, 3))
    # task3 = asyncio.create_task(fetch_data(3, 1))

    # result1 = await task1
    # result2 = await task2
    # result3 = await task3
    
    # print(result1, result2, result3)
    
    results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3))

    for result in results:
        print(f"Received result: {result}")
    
asyncio.run(main())