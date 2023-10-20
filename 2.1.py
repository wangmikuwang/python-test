grade = int(input())
if grade <0 or grade >100:
    print('错误的输入')
else:
    grade//= 10
    if grade == 9 or grade == 10:
        print('优秀')
    elif grade == 8:
        print('良')
    elif grade == 7:
        print('中')
    elif grade == 6:
        print('及格')
    elif grade >=0 and grade <6:
        print('不及格')