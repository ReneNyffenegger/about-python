src = '''
num =  42
txt = 'Hello world'
print(f'num = {num}, txt = {txt}')
'''

code = compile(src, '?', 'exec')

print(type(code))
#
# <class 'code'>

eval(code)
#
# num = 42, txt = Hello world
