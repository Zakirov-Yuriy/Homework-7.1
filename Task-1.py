# Задача-1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random
numbers = [random.randint(-100, 100) for _ in range(10)]

def bubble_reverse(num_):
    for j in range(len(num_) - 1):
        for i in range(len(num_) - 1 - j):
            if num_[i] < num_[i + 1]:
                num_[i], num_[i + 1] = num_[i + 1], num_[i]
    return num_

print('Исходный массив:', numbers)
print('Обратная пузырьковая:', bubble_reverse(numbers[:]))
