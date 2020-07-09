distance = int(input("Введите количество километров первого дня тренировки: "))
result = int(input("Введите желаемое количество километров, которое вы хотите достичь: "))
i = 1
while distance < result:
    distance + distance * 0.1
    distance *= 1.1
    i +=1
print(f"У вас все получится на {i} день!")
