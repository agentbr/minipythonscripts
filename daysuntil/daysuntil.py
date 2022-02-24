from datetime import date
f_date = date.today()
l_date = date(2022, 4, 16)
delta = l_date - f_date
print(delta.days)
print('Days until baptism')

from datetime import date
f_date = date.today()
l_date = date(2022, 10, 24)
delta = l_date - f_date
print(delta.days)
print('Days until birthday')

from datetime import date
f_date = date.today()
l_date = date(2022, 12, 25)
delta = l_date - f_date
print(delta.days)
print('Days until Christmas')
