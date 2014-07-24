#/usr/bin/python
#
#  Does python pass by value or by reference?
#
#  Output of program is
#
#     B[two] = 2
#     B[one] = 1
#   
#

def f(X, k, v):
    X[k] = str(v)

A=dict()

f(A, 'one', 1)

B=A

f(A, 'two', 2)

for k in B:
    print "  B["+k+"] = " + B[k]


    
