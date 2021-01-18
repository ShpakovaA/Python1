def common (a,b):
    return list(set(a) & set(b))
a = [7,6,5,4,6,8,9]
b = [9,9,8,7,7]
print(common (a,b))