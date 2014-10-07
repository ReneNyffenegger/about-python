def X():
    pass

def Y():
    global y
    pass
    y = 42

X()
Y()
print y  # 42
