scores = []
while True:
    score = float(input("请输入学生成绩（负数表示结束输入）: "))
    if score < 0:
        break
    scores.append(score)
print("及格的成绩:")
for score in scores:
    if score >= 60:
        print(score)