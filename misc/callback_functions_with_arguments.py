def math_op(func, operand_1, operand_2): return func(operand_1, operand_2)

def plus(a, b): return a+b
def mult(a, b): return a*b


print (math_op(plus, 4, 5)) #  9
print (math_op(mult, 4, 5)) # 20
