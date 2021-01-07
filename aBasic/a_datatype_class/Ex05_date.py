"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

from datetime import date, timedelta

today = date.today()
print('today is ', today)
print('연도 ', today.year)
print('월 ', today.month)
print('일 ', today.day)

# 날짜계산 -> timedalta
# from datetime import timedelta
print('어제', today + timedelta(days=-1))
print('일주일후', today+timedelta(days=+7))
print('10일전', today+timedelta(days=-10))

from dateutil.relativedelta import relativedelta
after_month = today + relativedelta(months=1)
print(after_month)
print()

#----------------------------------------------------
# 날짜 형식 출력 ( strftime() )
from datetime import datetime
today = datetime.today()
print(today.strftime("%m-%d-%Y %H : %M"))
print()

# 문자열을 날짜형으로 변환 ( ***** strptime() )
days = '2021-01-08 12:50'
mydate = datetime.strptime(days,'%Y-%m-%d %H:%M')
print(mydate)
print(type(mydate))