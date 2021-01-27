def common (a, b):
    return list(set(a) & set(b))
import random
a = [random.randrange(1, 50, 1) for i in range(20)]
b = [random.randrange(1, 50, 1) for i in range(20)]
print(a)
print(b)
print(common(a, b))