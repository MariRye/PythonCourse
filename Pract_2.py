# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

print("Please, enter a sequence of numbers")
sequence_1 = [int(i) for i in input().split()]
sum = 0
for i in range (len(sequence_1)):
    if (not (i % 2)):
        sum += sequence_1[i]

print(sum)

# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

print("Please, enter a sequence of numbers")
sequence_2 = [int(i) for i in input().split()]
result = []
mid_of_seq = len(sequence_2)//2
if (len(sequence_2) % 2): mid_of_seq = len(sequence_2)//2 + 1
for i in range (mid_of_seq):
    res = sequence_2[i]*sequence_2[len(sequence_2)-i-1]
    result.append(res)

print(result)

# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print("Please, enter a sequence of numbers")
sequence_3 = [float(i) for i in input().split()]

min = 1
max = 0
for el in sequence_3:
    if el % 1 == 0:
        continue
    if el - int(el) < min:
        min = round(el - int(el), 2)
        continue
    if el - int(el) > max:
        max = round(el % 1, 2)

print(f"{max} - {min} = {round(max - min, 2)}")


#Написать программу преобразования десятичного числа в двоичное

num = int(input("input num: "))
b = ''
while num != 0:
    b += str(num % 2)
    num = num // 2
print('0b' + b[::-1])