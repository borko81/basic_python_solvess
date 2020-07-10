shape = input()

if shape == 'square':
    size = float(input())
    print('{0:.3f}'.format(size*size))
elif shape == 'rectangle':
    w = float(input())
    h = float(input())
    print('{0:.3f}'.format(w*h))
elif shape == 'circle':
    r = float(input())
    import math
    print('{0:.3f}'.format(r*r*math.pi))
elif shape == 'triangle':
    w = float(input())
    h = float(input())
    print('{0:.3f}'.format(w*h/2))
else:
    pass

