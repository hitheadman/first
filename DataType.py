per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Money = "))
for key in per_cent:
    per_cent[key] = money/100*per_cent[key]
deposite = [round(x, 2) for x in list(per_cent.values())]
print(deposite)
print("Максимальная сумма, которую вы можете заработать — ", max(deposite))
