import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

Discriminant = b ** 2 - 4 * a * c

if Discriminant > 0:
    x1 = (-b + math.sqrt(Discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(Discriminant)) / (2 * a)
    print(f'два корня уравнения x1 = {x1}, x2 = {x2}')
elif Discriminant == 0:
    x = -b / (2*a)
    print(f' только один корень x = {x}')
else:
    print('корней нет')