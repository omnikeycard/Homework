timer = int(input('Введите время в секундах: '))
hour = timer // 3600
timer = timer % 3600
minute = timer // 60
timer = timer % 60
second = timer 
print(f'Время: {hour}:{minute}:{second}')
input()
