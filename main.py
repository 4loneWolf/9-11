import random

def generate_array(size, min_value, max_value, bool=False):
    if bool:
        return [[random.randint(min_value, max_value) for _ in range(size)] for _ in range(size)]
    else:
        return [random.randint(min_value, max_value) for _ in range(size)]

def main():
    print(generate_array(5, 0, 10))
    print(generate_array(5, 0, 10, True))

main()