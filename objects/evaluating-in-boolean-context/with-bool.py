class with_bool:

    def __init__(self, cntTrue):
        self.cntTrue = cntTrue

    def __bool__(self):

        print("__bool__: cntTrue = " + str(self.cntTrue))

        self.cntTrue -= 1
        return self.cntTrue >= 0


W = with_bool(4)


while W:
    print("Still in loop")

print("Loop exited")
#
#  __bool__: cntTrue = 4
#  Still in loop
#  __bool__: cntTrue = 3
#  Still in loop
#  __bool__: cntTrue = 2
#  Still in loop
#  __bool__: cntTrue = 1
#  Still in loop
#  __bool__: cntTrue = 0
#  Loop exited
