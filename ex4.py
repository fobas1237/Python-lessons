digit = abs(int(input("Введите целое положительное число: ")))

max = digit % 10

while digit >= 1:
    digit = digit // 10
    if digit % 10 > max:
        max = digit % 10
    if digit > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break
