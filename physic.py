def decorator(CalcAcceleration):
    def wrapper():
        a = CalcAcceleration(v0, v1, t)
        print('Пройденный путь:', abs(a)*(t**2)/2)
    return wrapper

@decorator
def CalcAcceleration(v0, v1, t):
    return (v1-v0)/t

try:
    v0 = int(input())
    v1 = int(input())
    t = int(input())
    if (t == 0): raise ZeroDivisionError
except ValueError:
    print('Вы должны ввести числа.')
except ZeroDivisionError:
    print('Время не может быть равно нулю.')
else: CalcAcceleration()
input()
