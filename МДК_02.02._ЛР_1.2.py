import random

number = int(input("Введите свой номер по журналу: "))
print("Число элементов в списке:", number + 10)
print("Сгенерированный список")
min_value = 5
max_value = (number + 10) * 100  # № по журналу * 100
print("Минимальный элемент в списке:", min_value, ", максимальный элемент:", max_value)
list = [random.randint(min_value, max_value) for _ in range(number + 10)]
print(list)