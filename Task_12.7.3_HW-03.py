per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print('Bank percentage: ', per_cent)
money = int(input('Please input initial amount of money for the deposit calculation:'))

print('\nmoney =', money)

s = [round(money * per_cent['ТКБ'] / 100),
     round(money * per_cent['СКБ'] / 100),
     round(money * per_cent['ВТБ'] / 100),
     round(money * per_cent['СБЕР'] / 100)
     ]
print('\ndeposit =', s)
print('\nThe maximum amount you can earn -', max(s))