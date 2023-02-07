# Задиние к модулю 18.8.18
tickets = int(input('Введите количество билетов: '))
age = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст участника конференции №{i + 1}: '))
    age.append(input_value)
    def prise(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        else:
            return 1390
    total_amount = sum(map(prise, age))
discount = int(total_amount * 0.9)
if tickets > 3:
    print('Цена за все билеты с учетом скидки: ', discount, "руб.")
else:
    print('Цена за все билеты: ', total_amount, "руб.")
