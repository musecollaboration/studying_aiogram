import asyncio


async def coroutine(i):
    await asyncio.sleep(1)
    print(f'Coroutine {i} is done')


async def main(num):
    task = [coroutine(i) for i in range(num)]
    await asyncio.gather(*task)


asyncio.run(main(10))
