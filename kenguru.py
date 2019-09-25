
msg = 'Введите начальные данные:\n'

while True:
    try:
        x1, v1, x2, v2 = map(int, input(msg).split())
    except Exception as e:
        msg = f'Неверный формат введенных данных ({e}). Введите заново:\n'
    else:
        if v1<0 and v2>0 or v1>0 and v2<0:
            msg = 'Кенгуру не готовы двигаться в одном направлении. Введите корректные данные:\n'
        else:
            break

if v2 != v1:
    n = (x1 - x2)/(v2 - v1)
    if n >= 0 and n.is_integer():
        print('YES')
    else:
        print('NO')
else:
    if x1 == x2:
        print('YES')
    else:
        print('NO')
