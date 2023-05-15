import asyncio

async def foo():
    print('Comenzando foo')
    await asyncio.sleep(1)
    print('Terminando foo')

async def bar():
    print('Comenzando bar')
    await asyncio.sleep(2)
    print('Terminando bar')

async def main():
    task1 = asyncio.create_task(foo())
    task2 = asyncio.create_task(bar())

    await task1
    await task2

asyncio.run(main())