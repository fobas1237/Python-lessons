quest = int(input("Введите время в секундах, чтобы перевести его в минуты, секунды и часы: "))

hours = quest // 3600
minutes = (quest - hours * 3600) // 60
seconds = quest - (hours * 3600 + minutes * 60)
print(f"Время: {hours}: {minutes}: {seconds}")
