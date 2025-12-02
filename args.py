
def calculate(operator, *args): # Non-Keyword argument
    if operator == '+':
        return sum(args)
    elif operator == '*':
        total = 1
        for i in args:
            total *= i
        return total
    
    return sum(args)

t = calculate('*', 1, 2, 3, 4, 5)
print(t)


t = (1, 2, 3, 4)

print(*t) # print(1, 2, 3, 4)
print(t)  # print((1, 2, 3, 4))

# packing, unpacking
