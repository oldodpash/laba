import string
import math

symbols = string.ascii_uppercase
new_symbols = []
new_symbols_special = []
for i in range(10):
    new_symbols_special.append(i)
for a in symbols:
    new_symbols_special.append(a)
    new_symbols.append(a)
for a in symbols:
    for b in symbols:
        new_symbols_special.append(a + b)
        new_symbols.append(a + b)
index1 = 0
massiv = []
a, b, i = '', '', 0


def converter_from_10(n, to_base, fl=False):
    global index1, massiv
    index1 += 1
    if not hasattr(converter_from_10, 'table'):
        converter_from_10.table = new_symbols_special
    x, y = divmod(n, to_base)
    massiv.append(str(y))
    if not fl:
        print(f'{index1}. Текущие показатели: Частное - {x}, остаток - {y}')
    if x:
        if fl:
            return converter_from_10(x, to_base, fl=True) + converter_from_10.table[y]
        return converter_from_10(x, to_base) + converter_from_10.table[y]
    else:
        return converter_from_10.table[y]


def convert_from_10_with_point(n, to_base):
    iterations = 0
    sp = []
    while iterations < 5:
        iterations += 1
        a, n = map(str, str(float(n) * to_base).split('.'))
        if int(a) > to_base - 1 and to_base < 10 or int(a) > 9 and to_base > 10:
            if to_base > 10:
                a = new_symbols[int(a) - 10]
            else:
                a = start_from_10(int(a), to_base, fl=True)
        n = '0.' + n
        sp.append(''.join(a))
        print(f'{iterations}. Текущие показатели: Произведение - {a}, новое делимое - {n}')
    print(f'{iterations + 1}. Соединим получившиеся значения в прямом порядке: {" + ".join(sp)} = {"".join(sp)}')
    return "".join(sp)


def start_from_10(n, to_base, fl=False):
    global massiv, index1
    massiv = []
    index1 = 0
    if not fl:
        print('-' * 60)
        print(f'Шаги перевода числа {n} из системы счисления 10 в {to_base}:')
    if '.' not in str(n):
        res = converter_from_10(n, to_base)
        if not fl:
            print(
                f'{index1 + 1}. Соединим получившиеся значения в обратном порядке: {" + ".join(massiv[::-1])} = {"".join(massiv[::-1])}')
            print(f'+ Результат данного преобразования: {"".join(massiv[::-1])}')
    else:
        result = convert_from_10_with_point(n, to_base)
        try:
            massiv = []
            index1 = 0
            converter_from_10(int(n), to_base, fl=True)
            points = len("".join(massiv[::-1]))
        except:
            points = 0
        if str("".join(massiv[::-1])) == '0':
            points = 0
        if points == 0:
            print(f'+ Результат данного преобразования: 0.{result}')
        else:
            print(f'+ Результат данного преобразования: {result[:points]}.{result[points::]}')
    if not fl:
        print('-' * 60)
    return "".join(massiv[::-1])


def to_digit(s):
    if s.isdigit():
        return int(s)
    return new_symbols.index(s) + 10


def converter_to_10(n, from_base):
    print('-' * 60)
    print(f'Шаги перевода числа {n} из системы счисления {from_base} в 10:')
    if from_base == 'BERG':
        from_base = (1 + math.sqrt(5)) / 2
    if '.' in n:
        a, b = map(str, n.split('.'))
    else:
        a = n
        b = 'null'
    sum1 = 0
    sums_sp = []
    sp = []
    idx = 1
    n = n.replace('.', '')
    for iii in n:
        sp.append(
            f'{idx}. {to_digit(iii)} * {from_base}^{len(a) - idx} = {to_digit(iii) * from_base ** (len(a) - idx)}')
        sums_sp.append(to_digit(iii) * from_base ** (len(a) - idx))
        sum1 += to_digit(iii) * from_base ** (len(a) - idx)
        idx += 1
    print(*sp, sep='\n')
    print(f'{idx}. Суммируем все получившиеся значения: ', end='')
    for iii in range(len(sums_sp)):
        print(sums_sp[iii], end=' ')
        if iii == len(sums_sp) - 1:
            break
        print('+', end=' ')
    print(f'= {sum1}\n+ Результат данного преобразования: {sum1}')
    print('-' * 60)
    return sum1


def fi_to_ten(n):
    print(f'Шаги перевода числа {n} из системы счисления FIB в 10:')
    f0, f1 = 0, 1
    i = 0
    n = n[::-1]
    res = 0
    while i < len(n):
        f0, f1 = f1, f0 + f1
        if n[i] == '1':
            res += f1
            print('Текущее значение нового числа:', res)
        i += 1
    print('Получившийся результат:', res)
    return res


def ten_to_fi(n):
    print(f'Шаги перевода числа {n} из системы счисления 10 в FIB:')
    n = int(n)
    f0, f1 = 0, 1
    resnum = []
    num = -1
    finres = ''
    while n != 0:
        while f1 <= n:
            f0, f1 = f1, f0 + f1
            num += 1
            if f1 > n:
                n -= f0
                resnum.append(num)
                f0, f1 = 0, 1
                num = -1
    i = resnum[0]
    print('Полученные числа ФИБ для вычисления:', resnum)
    while i > 0:
        k = 0
        check = False
        while k < len(resnum):
            if i == resnum[k]:
                finres += '1'
                print('Текущее значение нового числа:', finres)
                check = True
            k += 1

        if check is False:
            finres += '0'
            print('Текущее значение нового числа:', finres)
        i -= 1
    print('Получившийся результат:', finres)
    return finres
