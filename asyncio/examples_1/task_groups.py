import asyncio

async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data.")
    await asyncio.sleep(sleep_time)
    return {"data": f"Sample data from coroutine {id}", "id": id}

async def main():
    tasks = []
    # Task Group provides built-in error handling
    # The TaskGroup class is used to manage a group of tasks, 
    # allowing the main coroutine to wait for all tasks to complete and collect their results. 
    # This provides a way to run multiple tasks concurrently and handle their results in a structured way.
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
    
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received result: {result}")
    
asyncio.run(main())