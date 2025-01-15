import random
from concurrent.futures import ThreadPoolExecutor

def generate_array(size, min_value, max_value, bool=False):
    """
    Генерирует массив случайных чисел.

    :size: Размер массива.
    :min_value: Минимальное значение элементов массива.
    :max_value: Максимальное значение элементов массива.
    :bool: Флаг для генерации массива подмассивов.
    :return: Сгенерированный массив.
    """
    if bool:
        return [[random.randint(min_value, max_value) for _ in range(size)] for _ in range(size)]
    else:
        return [random.randint(min_value, max_value) for _ in range(size)]

def input_array(bool=False):
    """
    Вводит массив с клавиатуры.

    :param bool: Флаг для ввода массива подмассивов.
    :return: Введенный массив.
    """
    array = []
    if bool:
        rows = int(input("Введите количество подмассивов: "))
        columns = int(input("Введите количество элементов массива: "))
        for a in range(rows):
            for b in range(columns):
                array.append(int(input(f"Введите элемент массива [{a}][{b}]: ")))
    else:
        size = int(input("Введите размер массива: "))
        for _ in range(size):
            array.append(int(input("Введите элемент массива: ")))

    return array

def create_array(bool=False):
    """
    Создает массив, выбирая между вводом с клавиатуры и генерацией случайным образом.

    :param bool: Флаг для создания массива подмассивов.
    :return: Созданный массив.
    """
    choice = input("Хотите ввести массив вручную (m) или сгенерировать случайным образом (r)? ")
    if choice.lower() == 'm':
        return input_array(bool)
    elif choice.lower() == 'r':
        size = int(input("Введите размер массива: "))
        min_value = int(input("Введите минимальное значение: "))
        max_value = int(input("Введите максимальное значение: "))
        return generate_array(size, min_value, max_value, bool)
    else:
        print("Неверный выбор. Попробуйте снова.")
        return create_array(bool)

def count_subarrays_with_sum_worker(subarray, target_sum):
    """
    Рабочая функция для подсчета подмассивов с суммой, равной target_sum.

    :param subarray: Подмассив для обработки.
    :param target_sum: Заданное значение суммы.
    :return: Количество подмассивов с заданной суммой.
    """
    count = 0
    current_sum = 0
    start = 0
    for mainarray in subarray:
        for end in range(len(mainarray)):
            current_sum += mainarray[end]
            while current_sum > target_sum and start <= end:
                current_sum -= mainarray[start]
                start += 1
            if current_sum == target_sum:
                count += 1
    return count

def count_subarrays_with_sum(array, target_sum):
    """
    Подсчитывает количество подмассивов, сумма элементов которых равна заданному числу,
    используя многопоточность через ThreadPoolExecutor.

    :param array: Массив подмассивов для обработки.
    :param target_sum: Заданное число для проверки суммы подмассивов.
    :return: Количество подмассивов с заданной суммой.
    """
    num_threads = 4  # Количество потоков
    subarrays = [array[i::num_threads] for i in range(num_threads)]  # Разделение массива на части

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(lambda subarray: count_subarrays_with_sum_worker(subarray, target_sum), subarrays))

    return sum(results)

def count_common_elements_worker(array1_part, array2):
    """
    Рабочая функция для подсчета общих элементов в двух массивах, включая перевернутые числа.

    :param array1_part: Часть первого массива для обработки.
    :param array2: Второй массив для сравнения.
    :return: Количество общих чисел.
    """
    def is_reversed(num1, num2):
        """
        Проверяет, является ли одно число перевернутой версией другого.

        :param num1: Первое число.
        :param num2: Второе число.
        :return: True, если num1 является перевернутой версией num2, иначе False.
        """
        return str(num1)[::-1] == str(num2)

    common_count = 0
    for num1 in array1_part:
        for num2 in array2:
            if num1 == num2 or is_reversed(num1, num2):
                common_count += 1
                break
    return common_count

def count_common_elements(array1, array2):
    """
    Подсчитывает количество общих чисел в двух массивах, включая перевернутые версии,
    используя многопоточность через ThreadPoolExecutor.

    :param array1: Первый массив.
    :param array2: Второй массив.
    :return: Количество общих чисел.
    """
    num_threads = 4  # Количество потоков
    array1_parts = [array1[i::num_threads] for i in range(num_threads)]  # Разделение массива 1 на части

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(lambda part: count_common_elements_worker(part, array2), array1_parts))

    return sum(results)

def can_form_number_worker(array1_part, array2_part, array3_part):
    """
    Рабочая функция для проверки, можно ли получить число из третьего массива арифметическими преобразованиями
    с числами из двух других массивов.

    :param array1_part: Часть первого массива для обработки.
    :param array2_part: Часть второго массива для обработки.
    :param array3_part: Часть третьего массива для проверки.
    :return: Список результатов для части массива.
    """
    def can_form(num1, num2, target):
        """
        Проверяет, можно ли получить число target арифметическими преобразованиями с числами num1 и num2.

        :param num1: Первое число.
        :param num2: Второе число.
        :param target: Целевое число.
        :return: True, если можно получить число target, иначе False.
        """
        return num1 + num2 == target or num1 - num2 == target or num2 - num1 == target or num1 * num2 == target or (num2 != 0 and num1 / num2 == target) or (num1 != 0 and num2 / num1 == target)

    results = [can_form(array1_part[i], array2_part[i], array3_part[i]) for i in range(len(array3_part))]
    return results

def can_form_number(array1, array2, array3):
    """
    Проверяет, можно ли получить число из третьего массива арифметическими преобразованиями
    с числами из двух других массивов, используя многопоточность через ThreadPoolExecutor.

    :param array1: Первый массив.
    :param array2: Второй массив.
    :param array3: Третий массив.
    :return: Список результатов проверки.
    """
    num_threads = 4  # Количество потоков
    array1_parts = [array1[i::num_threads] for i in range(num_threads)]  # Разделение массива 1 на части
    array2_parts = [array2[i::num_threads] for i in range(num_threads)]  # Разделение массива 2 на части
    array3_parts = [array3[i::num_threads] for i in range(num_threads)]  # Разделение массива 3 на части

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(lambda p1, p2, p3: can_form_number_worker(p1, p2, p3), array1_parts, array2_parts, array3_parts))
    print(results)
    # Объединяем все результаты из частей
    final_results = [result for sublist in results for result in sublist]
    print(final_results)
    return final_results

def main():
    while True:
        print("Выберите задание:")
        print("1. Проверить, сколько подмассивов из массива в сумме могут давать заданное число.")
        print("2. Проверить, сколько у массивов общих чисел, включая перевернутые версии.")
        print("3. Проверить, можно ли получить число из третьего массива арифметическими преобразованиями с числами из двух других массивов.")
        print("4. Завершить работу программы.")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            array = create_array(True)
            target_sum = int(input("Введите число для проверки суммы подмассивов: "))
            result = count_subarrays_with_sum(array, target_sum)
            print(f"Количество подмассивов с суммой {target_sum}: {result}")
        elif choice == '2':
            array1 = create_array()
            array2 = create_array()
            result = count_common_elements(array1, array2)
            print(f"Количество общих чисел: {result}")
        elif choice == '3':
            array1 = create_array()
            array2 = create_array()
            array3 = create_array()
            results = can_form_number(array1, array2, array3)
            for i, result in enumerate(results):
                print(f"Число {array3[i]} может быть получено: {result}")
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

main()