
def calculate(a, b, c=21, *args, **kwargs):
    print(a, b)
    print(c)
    print(args)
    print(kwargs)


calculate('a', 2, 3, 4, 5, x=1, y=2, z=3)
