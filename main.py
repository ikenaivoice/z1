abc = [8, 2, 2, 7, 9, 12, 11, 13, 20, 16, 14, 19, 24, 31, 23, 13]
abc = sorted(abc, reverse=True)
abcmax = 0
for i in range(len(abc)):
    for j in range(i + 1, len(abc)):
        for k in range(j + 1, len(abc)):
            a = abc[i]
            b = abc[j]
            c = abc[k]
            if a + b > c and a + c > b and b + c > a:
                p = (a + b + c) / 2
                s = (p * (p - a) * (p - b) * (p - c)) ** (1 / 2)
            if s > abcmax:
                abcmax = s
print("Максимальная площадь треугольника равна", abcmax)