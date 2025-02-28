import random

def generate_random_list(n):
    """Генерирует список из n случайных чисел в диапазоне от 5 до 1000."""
    min_value = 5
    max_value = (n - 10) * 100  # № по журналу * 100
    print("Минимальный элемент в списке:", min_value, ", максимальный элемент:", max_value)
    return [random.randint(min_value, max_value) for _ in range(n)]

number = int(input("Введите свой номер по журналу: "))
print("Число элементов в списке:", number + 10)
print("Сгенерированный список")
list = generate_random_list(number + 10)
print(list)