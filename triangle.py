import math
while True:
    try:
        n = int(input('ВВЕДИТЕ КОЛИЧЕСТВО ЧИСЕЛ: '))
    except Exception:
        print('ВВОДИТЕ ТОЛЬКО ЦЕЛЫЕ ЧИСЛА')
    else:
        if n <= 0:
            print('ВВОДИТЕ ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ ЧИСЛА!')
        elif 0 < n <= 2:
            print('ВВОДИТЕ ЧИСЛА БОЛЬШЕ 3!')
        else:
            break
a = b = c = []
for i in range(n):
    Loop = True
    while Loop:
        try:
            num = int(input('ВВЕДИТЕ ЧИСЛО: '))
        except Exception:
            print('ВВОДИТЕ ТОЛЬКО ЦЕЛЫЕ ЧИСЛА!')
        else:
            if num <= 0:
                print('ВВОДИТЕ ТОЛЬКО ПОЛОЖИТЕЛЬНЫЕ ЧИСЛА!')
            else:
                a.append(num)
                Loop = False

m = m1 = m2 = m3 = 0

for i in range(0, len(a)):
    for j in range(0,len(a)):
        for g in range(0, len(a)):
            if (i == j) or (j == g) or (i == g):
                continue
            if (a[i] + a[j]) > a[g] and (a[j] + a[g]) > a[i] and (a[i] + a[g]) > a[j]:
                p = (a[i] + a[j] + a[g]) // 2
                s = math.sqrt(abs(p * (p - a[i]) * (p - a[j]) * (p - a[g])))
                m = max(s, m)
                if s == m:
                    m1 = a[i]
                    m2 = a[j]
                    m3 = a[g]
                else:
                    print('ТРЕУГОЛЬНИК НЕ СУЩЕСТВУЕТ')
print(m)
print(m1, m2, m3)


