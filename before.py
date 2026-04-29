# 包含代码坏味道的原始代码
def calculate_student_score(math, english, science):
    unused_var = "test"  # 未使用变量（CodeQL 可检测）
    total = math + english + science
    average = total / 3
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"总分：{total}")
    print(f"平均分：{average}")
    print(f"等级：{grade}")
    return total, average, grade

def calculate_teacher_score(work1, work2, work3):
    unused_var = "test"  # 未使用变量（CodeQL 可检测）
    total = work1 + work2 + work3
    average = total / 3
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"总分：{total}")
    print(f"平均分：{average}")
    print(f"等级：{grade}")
    return total, average, grade

if __name__ == "__main__":
    calculate_student_score(85, 92, 88)
    calculate_teacher_score(90, 85, 95)