from random import randint

name1 = input('Введите имя первого игрока: ')
name2 = input('Введите имя второго игрока: ')
q1 = 0
q2 = 0
igrok = randint(1, 2)
a = int(input('Введите количество конфет: '))
while a <= 28:
    a = int(input('Вы ввели неверное количество конфет. Попробуйте заново!'))
if igrok == 1:
    print('Первый ход делает ', name1)
else:
    print('Первый ход делает ', name2)

while a >0:
    if a > 28:
        igrok1 = int(input(f'На столе осталось {a} конфет. Возьмите не больше 28 конфет, сколько конфет взял игрок, {name1} ? '))
        while igrok1 < 0 or igrok1 > 28 or igrok1 > a:
            igrok1 = int(input('Вы берете неверное количество конфет! Попробуйте снова: '))
        a -= igrok1
        q1 += igrok1
        if a > 28:
            igrok2 = int(input(f'На столе осталось {a} конфет. Возьмите не больше 28 конфет, сколько конфет взял игрок, {name2} ? '))
            while igrok2 < 0 or igrok2 > 28 or igrok2 > a:
                igrok2 = int(input('Вы берете неверное количество конфет! Попробуйте снова: '))
            a -= igrok2
            q1 += igrok2
            if a <= 28:
                if igrok == 1:
                    print('Осталось ', a,' конфет, их забирает и побеждает:', name1)
                else:
                    print('Осталось ', a, ' конфет, их забирает и побеждает:', name2)
        else:
            if igrok == 1:
                print('Осталось ', a, ' конфет, их забирает и побеждает:', name2)
            else:
                print('Осталось ', a, ' конфет, их забирает и побеждает:', name1)