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

def count_subarrays_with_sum(array, target_sum):
    """
    Подсчитывает количество подмассивов, сумма элементов которых равна заданному числу.

    :param array: Массив подмассивов.
    :param target_sum: Заданное число для проверки суммы подмассивов.
    :return: Количество подмассивов с заданной суммой.
    """
    count = 0
    current_sum = 0
    start = 0
    for mainarray in array:
        for end in range(len(mainarray)):
            current_sum += mainarray[end]
            while current_sum > target_sum and start <= end:
                current_sum -= mainarray[start]
                start += 1
            if current_sum == target_sum:
                count += 1
    return count

def count_common_elements(array1, array2):
    """
    Подсчитывает количество общих чисел в двух массивах, включая перевернутые версии.

    :param array1: Первый массив.
    :param array2: Второй массив.
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
    for num1 in array1:
        for num2 in array2:
            if num1 == num2 or is_reversed(num1, num2):
                common_count += 1
                break
    return common_count

def can_form_number(array1, array2, array3):
    """
    Проверяет, можно ли получить число из третьего массива арифметическими преобразованиями с числами из двух других массивов.

    :param array1: Первый массив.
    :param array2: Второй массив.
    :param array3: Третий массив.
    :return: Список результатов проверки.
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
    print(array2)
    results = []
    for i in range(len(array3)):
        num1 = array1[i]
        num2 = array2[i]
        target = array3[i]
        results.append(can_form(num1, num2, target))
    return results

def main():
    while True:
        print("Выберите задание:")
        print("1. Проверить, сколько подмассивов из массива в сумме могут давать заданное число.")
        print("2. Проверить, сколько у массивов общих чисел, включая перевернутые версии.")
        print("3. Проверить, можно ли получить число из третьего массива арифметическими преобразованиями с числами из двух других массивов.")
        print("4. Завершить работу программы.")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            with ThreadPoolExecutor() as executor:
                array = executor.submit(create_array, True).result()
            # array = create_array(True)
            target_sum = int(input("Введите число для проверки суммы подмассивов: "))
            result = count_subarrays_with_sum(array, target_sum)
            print(f"Количество подмассивов с суммой {target_sum}: {result}")
        elif choice == '2':
            with ThreadPoolExecutor() as executor:
                array1 = executor.submit(create_array).result()
                array2 = executor.submit(create_array).result()
            result = count_common_elements(array1, array2)
            print(f"Количество общих чисел: {result}")
        elif choice == '3':
            with ThreadPoolExecutor() as executor:
                array1 = executor.submit(create_array).result()
                array2 = executor.submit(create_array).result()
                array3 = executor.submit(create_array).result()
            results = can_form_number(array1, array2, array3)
            for i, result in enumerate(results):
                print(f"Число {array3[i]} может быть получено: {result}")
        elif choice == '4':
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

with ThreadPoolExecutor() as executor:
    executor.submit(main)