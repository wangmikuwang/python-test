student_scores = {
    "张三": {"语文": 85, "数学": 90, "英语": 92},
    "李四": {"语文": 78, "数学": 82, "英语": 88},
    "王五": {"语文": 65, "数学": 70, "英语": 72},
    "赵六": {"语文": 59, "数学": 63, "英语": 67},
    "孙七": {"语文": 93, "数学": 95, "英语": 97}
}
print("成绩不及格的学生信息如下：")
for name, scores in student_scores.items():
    if scores["语文"] < 60 or scores["数学"] < 60 or scores["英语"] < 60:
        print(name, scores)
subjects = ["语文", "数学", "英语"]
for subject in subjects:
    print(f"按{subject}成绩排序的结果如下：")
    sorted_list = sorted(student_scores.items(), key=lambda x: x[1][subject], reverse=True)
    for name, scores in sorted_list:
        print(name, scores[subject])
