import asyncio

async def async_func():

      print('Hello…')
      await asyncio.sleep(1)
      print('…World')


co_routine = async_func()
#
#  <class 'coroutine'>

print(type(co_routine))

asyncio.run(co_routine)
