# Создайте программу для игры с конфетами человек против человека.
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход 
# можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход.

from random import *
import os

text1 = ('Правила игры:\n'
         'Есть 117 конфет, игроки берут их поочередно,\n'
         'причем, за один раз можно взять не больше 28 конфет.\n'
         'Выигрывает тот, кто последним ходом заберет все конфеты.\n')
print(text1)

message = ['твоя очередь']


def player_vs_player():
    candies_total = 117
    max_take = 28
    count = 0
    player_1 = input('\nВведите свое имя: ')
    player_2 = input('\nВведите имя соперника: ')

    print('\nОпределим кто первый начнет игру.\n')

    x = randint(1, 2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
    print(f'\n{lucky} ходит первым!')

    while candies_total > 0:
        if count == 0:
            step = int(input(f'\n{choice(message)} {lucky} = '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай, можно взять только {max_take} конфет, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nосталось еще {candies_total} конфет')
            count = 1
        else:
            print('Конец! конфет больше нет')

        if count == 1:
            step = int(input(f'\n{choice(message)}, {loser} '))
            if step > candies_total or step > max_take:
                step = int(input(
                    f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
            candies_total = candies_total - step
        if candies_total > 0:
            print(f'\nОсталось еще {candies_total} конфет')
            count = 0
        else:
            print('Кончились конфетки!')

    if count == 1:
        print(f'{loser} ПОБЕДИЛ')
    if count == 0:
        print(f'{lucky} ПОБЕДИЛ')


player_vs_player()


def player_vs_bot():
    candies_total = 117
    max_take = 28
    player_1 = input('\nВведите свое имя: ')
    player_2 = 'Компьютер'
    players = [player_1, player_2]
    print(f'\nНачинаем! {player_1} против {player_2}\n')
    print('\nОпределим кто начинает игру.\n')

    lucky = randint(-1, 0)

    print(f'Поздравляю {players[lucky + 1]} ты ходишь первым !')

    while candies_total > 0:
        lucky += 1

        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky % 2]} \nВсего {candies_total}. \n{choice(message)}: ')

            if candies_total < 29:
                step = candies_total
            else:
                delenie = candies_total // 28
                step = candies_total - ((delenie * max_take) + 1)
                if step == -1:
                    step = max_take - 1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(input(f'\nВаш ход, {players[lucky % 2]} \nОсталось {candies_total} {choice(message)}:  '))
            while step > max_take or step > candies_total:
                step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
        candies_total = candies_total - step

    print(f'Осталось {candies_total} \nПобедил {players[lucky % 2]}')


player_vs_bot()