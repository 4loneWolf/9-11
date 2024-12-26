import random

def generate_array(size, min_value, max_value, bool=False):
    if bool:
        return [[random.randint(min_value, max_value) for _ in range(size)] for _ in range(size)]
    else:
        return [random.randint(min_value, max_value) for _ in range(size)]

def input_array(bool=False):
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

def count_common_elements(array1, array2):
    def is_reversed(num1, num2):
        return str(num1)[::-1] == str(num2)

    common_count = 0
    for num1 in array1:
        for num2 in array2:
            if num1 == num2 or is_reversed(num1, num2):
                common_count += 1
                break
    return common_count

def can_form_number(array1, array2, array3):
    def can_form(num1, num2, target):
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
    array1 = generate_array(5, 1, 10)
    array2 = generate_array(5, 1, 10)
    array3 = generate_array(5, 1, 10)
    results = can_form_number(array1, array2, array3)
    for i, result in enumerate(results):
        print(f"Число {array3[i]} может быть получено: {result}")

main()