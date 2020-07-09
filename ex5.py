income = int(input("Введите выручку вашей фирмы: "))
costs = int(input("Введите издержки вашей фирмы: "))

if income > costs:
    print(f"Фирма работает с прибылью. Рентабильность фирмы равна {(income - costs) / income}")
    workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль в расчете на одного сторудника сотавила: {(income - costs) / workers:.2f}")
elif income <= costs:
    print("Сорри. В этот раз без прибыли, работаем лучше, ребята;(")
