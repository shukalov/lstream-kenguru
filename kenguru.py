

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

if x1<x2 and v1>v2 or x1>x2 and v2>v1:
    print('YES')
else:
    print('NO')
