import random
g = 'Да'
while g == 'Да':
    print('1-камень 2-ножницы 3-бумага')
    player = int(input('Ваш ход: '))
    ii = random.randint(1, 3)

    if ii == 3:
        if player == 1:
            print('Компьютер выбрал бумагу: Вы проиграли')
        elif player == 2:
            print('Компьютер выбрал бумагу: Вы выиграли')
        else:
            print('Компьютер выбрал бумагу: Ничья')
    elif ii == 2:
        if player == 1:
            print('Компьютер выбрал ножницы: Вы выиграли')
        elif player == 3:
            print('Компьютер выбрал ножницы: Вы проиграли')
        else:
            print('Компьютер выбрал ножницы: Ничья')
    else:
        if player == 2:
            print('Компьютер выбрал камень: Вы проиграли')
        elif player == 3:
            print('Компьютер выбрал камень: Вы выиграли')
        else:
            print('Компьютер выбрал камень: Ничья')

    g = input('Продолжить? (Да / Нет): ')
print('Хорошо')