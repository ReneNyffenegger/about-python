def F(p1, p2, p3, p4, p5):
    
    print(f'p1 = {p1}, p2 = {p2}, p3 = {p3}, p4 = {p4}, p5 = {p5}')

F( *( (x ** 2)+3 for x in range(5) ) )
