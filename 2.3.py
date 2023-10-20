import math

radius =float(input())
if radius >0:
    area=math.pi * radius **2
    rounded_area =round(area,2)
    print(rounded_area)
else:
    print('请输入大于零的整数或实数')