#TODO наладить цикл (вроде работает)
#TODO Мутация (Зделана)
#TODO условие вихода
#TODO Обработка списка
import random
from pprint import pprint
from numpy import arange
from numpy import any


def find_num(x: int):
    return x * 0.01 + (-5.12)


# Определение функции, зависящей от позиции на отрезке
def custom_function(x: float):
    return 0.2*x**4 + 0.3*x**3 - 1.6*x**2 + 0.6*x + 20

#
#Закидываем в список номер, позицию, фитнес-функцию, и двоичный код
def mutgim(mut_bin):
    mut_num = int(mut_bin, 2)

    position0 = find_num(mut_num)
    function_result0 = custom_function(position0)
    return [mut_num, position0, function_result0, mut_bin]


# Создание изначального списка
result_list = []

for i in range(1, 51):
    # Генерация случайного числа в диапазоне от 1 до 1024
    random_number = random.randint(1, 1024)

    position = find_num(random_number)

    # Вызов вашей функции с текущей позицией
    function_result = custom_function(position)

    # Перевод номера в двоичную систему
    binary_number = bin(random_number)[2:].zfill(10)

    # Добавление кортежа в список
    result_list.append([random_number, position, function_result, binary_number])

# Ограничение на количество итераций
min_list = []
delaitor = 2
iteration_limit = 100
for iteration in range(iteration_limit):
    # Нахождение минимального елемента в списке а также количество повторений
    min_result = min( result_list, key=lambda x: x[2])[2]
    repeat = result_list.count(min(result_list, key=lambda x: x[2]))
    # Добавление в список минимальных чисел
    min_list.append(min_result)

    # Проверка выхода
    if repeat >= 35 and (min_result == min(min_list) or any(min_result == min(min_list) + arange(0, 0.4, 0.1))):
        break

    new_list = []
    # Кроссовер и получение нового списка
    for _ in range(25):
        # Рандомный выбор двух элементов из списка с весами (обратное число от позиции на отрезке)
        selected_elements = random.choices(result_list, weights=[1 / r[2] for r in result_list], k=2)
        fir = selected_elements[0]
        sec = selected_elements[1]
        # Рандомный выбор числа k от 1 до длины двоичного числа
        k = random.randint(1, len(fir))

        # Меняем местами части двоичных чисел
        binary_number1 = fir[3][:k] + sec[3][k:]
        binary_number2 = sec[3][:k] + fir[3][k:]

        # Переводим новые двоичные числа в десятичные
        new_number1 = int(binary_number1, 2)
        new_number2 = int(binary_number2, 2)

        # Получаем позицию на отрезке, значение функции и двоичный код из новых чисел
        position1 = find_num(new_number1)
        position2 = find_num(new_number2)
        function_result1 = custom_function(position1)
        function_result2 = custom_function(position2)
        new_list.append([new_number1, position1, function_result1, binary_number1])
        new_list.append([new_number2, position2, function_result2, binary_number2])

    # МУТАЦИЯ
    if iteration % delaitor == 0 and iteration != 0:
        for q in range(0, 1):
            #Создаем index и вытягиваем двоичный код из списка
            mut_el = new_list[random.randint(0, 49)]
            key = random.randint(1, len(mut_el[3]) - 1)
            str = mut_el[3]

            # Присвоение полученой мутации и возыращение её всписок
            if str[key] == '1':
                sim = '0'
            else:
                sim = '1'
            if not key == 0 or key == len(str):
                mut_bin = str[:key] + sim + str[key+1:]
                new_list[new_list.index(mut_el)] = mutgim(mut_bin)

            elif key == 0:
                mut_bin = sim + str[key + 1:]
                new_list[new_list.index(mut_el)] = mutgim(mut_bin)
            else:
                mut_bin = str[:key] + sim
                new_list[new_list.index(mut_el)] = mutgim(mut_bin)

    result_list = new_list.copy()
    print(iteration, 'минимальное', min_result)
    if iteration == 50 :
        pprint(result_list)
        print('минимальніе числа',min_list)



# Вывод результата
min_find = min(min_list)

pprint(result_list)
print('Минимальніе числа',min_list)
print('Минимальное встреченое число', min_find)

print('Результат роботы програмы', min_result)
print('Количество повторений', repeat)



