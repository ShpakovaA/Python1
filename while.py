def function (a):
 while a < 10:
    a = a + 2
    if a > 10:
        print('дождались!', a)
    elif a < 10:
        print(a, "пока что нет")
function (3)
