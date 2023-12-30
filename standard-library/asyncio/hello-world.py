import asyncio

async def async_func():

      print('Hello…')
      await asyncio.sleep(1)
      print('…World')


co_routine = async_func()

print(type(co_routine))
#
#  <class 'coroutine'>

asyncio.run(co_routine)
