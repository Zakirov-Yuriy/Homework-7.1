# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
numbers = [random.randint(0, 50) for _ in range(10)]

def merge_sort(num_):
    if len(num_) > 1:
        center = len(num_) // 2
        left = num_[:center]
        right = num_[center:]

        merge_sort(left)
        merge_sort(right)

        a, b, c = 0, 0, 0

        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                num_[c] = left[a]
                a += 1
            else:
                num_[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            num_[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            num_[c] = right[b]
            b += 1
            c += 1
        return num_


print('Исходный массив:', numbers)
print('Сортировка слиянием:', merge_sort(numbers[:]))
