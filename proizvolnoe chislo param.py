def test(*args, **kwargs):    #Произвольное число параметров
    print(*args)
    for key, value in kwargs.items():
        print(key, value)


test("Пример ", ispolzovania="parametrov", raznogo="tipa")

print()


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(int(input("Введите число : "))))
