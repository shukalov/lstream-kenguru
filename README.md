# Требования
Есть два кенгуру на оси координат, готовые прыгать в одном направлении (например, в
положительном направлении). Первый кенгуру находится в положении x1 и прыгает на
расстояние v1 за прыжок. Анологично с первым кенгуру, второй находится изначально в
положении x2 и прыгает на v2 за прыжок. По заданным начальным положениям и
скоростям можете ли вы определить окажутся ли они в одном месте в одно и тоже время?

### Входные данные​

Stdin с четырьми целыми числами, разделенными пробелом формата: x1 v1 x2 v2

### Ограничения​

* − 10000 ≤ x1, x2 ≤ 10000
* − 10000 ≤ v1, v2 ≤ 10000

### Формат вывода​

В stdout YES, если кенгуру могут встретится в одном месте в одно и тоже время. И NO в
обратном случае.

### Примеры​

Вход: 0 3 4 2

Результат: YES

Вход: 0 2 5 3

Результат: NO

# Мои комментарии

Не очень понятно как расстояния v1, v2 могут быть отрицательным, поэтому предположу, что знак это направление прыжка, соответсвенно если v1 и v2 разных знаков, то кенгуры не готовы двигаться в одном направлении.

Соотсветсвенно, на мой взгляд, при одном направлении и при равном количестве прыжков (что также надеюсь подразумевается), задача сводится к тому, чтобы скорость(расстояние прыжка) кенгуру, который позади (по оси направления прыжков) была больше, чем скорость(расстояние прыжка), того, который впереди. Тогда кенгуру позади рано или поздно догонит первого и они встретятся.

Решение в kenguru.py.

Если что-то недопонял, или нужно доработать - доработаю. Буду благодарен за любую обратную связь, особенно за отрицательную.