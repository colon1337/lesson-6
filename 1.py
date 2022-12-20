def a():
    b=0
    print('Для остановки введите "Стоп"')
    while True:
        if b == 'Стоп':
            print('Преобразование окончено')
            break
        else:
            b=input('Введите строку:')
            c=b.encode('utf-8')
            print(c)
            b=c.decode()
            print(f'Первоначальная строка: {b}')
a()