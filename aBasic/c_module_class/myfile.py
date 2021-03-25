''' 모듈 참조하는 방식'''

# 1. 모듈 전체를 참조할 때
# import mymodule
#
# today = mymodule.get_weather()
# print('오늘은', mymodule.get_date()+'요일입니다')
# print('오늘의 날씨는', today)

# 2. 별칭부여 가능
# import mymodule as mm
#
# today = mm.get_weather()
# print('오늘은', mm.get_date()+'요일입니다')
# print('오늘의 날씨는', today)

# 3. 모듈에서 필요한 부분만 임포트
from aBasic.c_module_class.mypack.mymodule import get_weather, get_date

today = get_weather()
print('오늘은', get_date() + '요일입니다')
print('오늘의 날씨는', today)
