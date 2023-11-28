#TODO наладить цикл (вроде работает)
#TODO Мутация
#TODO условие вихода
#TODO Обработка списка
import random
from pprint import pprint


def find_num(x: int):
    return x * 0.01 + (-5.12)


# Определение функции, зависящей от позиции на отрезке
def custom_function(x: float):
    # Ваша формула здесь
    # Например, для примера используем квадрат позиции
    return 0.2*x**4 + 0.3*x**3 - 1.6*x**2 + 0.6*x + 20


def mutgim(mut_bin):
    mut_num = int(mut_bin, 2)
    position0 = find_num(mut_num)
    function_result0 = custom_function(position0)
    return [mut_num, position0, function_result0, mut_bin]

# Создание списка из 50 элементов
result_list = []

for i in range(1, 51):
    # Генерация случайного числа в диапазоне от 1 до 1054
    random_number = random.randint(1, 1054)

    position = find_num(random_number)

    # Вызов вашей функции с текущей позицией
    function_result = custom_function(position)

    # Перевод номера в двоичную систему
    binary_number = bin(random_number)[2:].zfill(11)

    # Добавление кортежа в список
    result_list.append([random_number, position, function_result, binary_number])

# Ограничение на количество итераций
iteration_limit = 100

# Цикл повторяется до тех пор, пока половина чисел не станет одинаковыми
for iteration in range(iteration_limit):

    new_list = []
    # Внутренний цикл для случайной замены двух элементов
    for _ in range(25):
        # Рандомный выбор двух элементов из списка с весами (обратное число от позиции на отрезке)
        selected_elements = random.choices(result_list, weights=[1 / r for r in range(1, 51)], k=2)
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
    if iteration % 4 == 0 and iteration != 0:
        for q in range(0, 1):
            #Создаем index и вытягиваем двоичный код из списка
            mut_el = new_list[random.randint(0, 49)]  #TODO кудато надо запихнуть
            key = random.randint(0, len(mut_el[3]) - 1)
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
    print(iteration)

    # Проверяем, половина чисел одинакова или нет
    #if sum(1 for original, updated in zip(original_list, result_list) if original == updated) >= len(result_list) / 2:
   #     break

# Вывод результата
pprint(result_list)



