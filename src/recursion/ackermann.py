def ackermann (m: int, n: int, indentation: int = None) -> int:
    if indentation is None:
        indentation = 0
    print('%sackermann(%d, %d)' % (' ' * indentation, m, n))
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1, indentation + 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1, indentation + 1), indentation + 1)
    
print('Starting with Ackermann function: m = 1, n = 1')
print(ackermann(1, 1))

print('\nStarting with Ackermann function: m = 2, n = 3')
print(ackermann(2, 3))

# print('\nStarting with Ackermann function: m = 3, n = 4')
# print(ackermann(3, 4))