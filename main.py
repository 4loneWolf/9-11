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

def count_subarrays_with_sum(array, target_sum):
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

def main():
    array1 = generate_array(5, 1, 10, True)
    num = 5
    print(count_subarrays_with_sum(array1, num))


main()