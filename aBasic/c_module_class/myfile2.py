import mypack.mymodule

today = mypack.mymodule.get_weather()
print('오늘의 날씨 :', today)
print('오늘은', mypack.mymodule.get_date()+'요일입니다')

from mypack.mymodule import get_weather as gw

print(gw())

import mypack.mymodule as mm

today = mm.get_weather()
print('오늘의 날씨 :', today)
print('오늘은', mm.get_date()+'요일입니다')