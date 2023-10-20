grades =[]
for _ in range(10):
  grade = float(input('请输入一个分数：'))
  grades.append(grade)
for grade in grades:
  if grade <0 or grade>100:
    print('错误的输入')
  else:
    if grade >=90:
      print(f'{grade}: 优秀')
    elif grade >=80:
      print(f'{grade}: 良好')
    elif grade >=70:
      print(f'{grade}: 中等')
    elif grade >=60:
      print(f'{grade}: 及格')
    else:
      print(f'{grade}: 不及格')