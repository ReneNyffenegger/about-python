def sayHello() -> str:
    return 'hello world'

print('sayHello() is supposed to return a {}'.format(sayHello.__annotations__['return'].__name__))
#
#  sayHello() is supposed to return a str
