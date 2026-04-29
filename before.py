# 包含代码坏味道的原始代码
def calculate_student_score(math, english, science):
    # 未使用的冗余变量
    unused_var = "test"
    # 计算总分
    total = math + english + science
    # 计算平均分
    average = total / 3
    # 判断等级
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"
    # 打印结果
    print(f"总分：{total}")
    print(f"平均分：{average}")
    print(f"等级：{grade}")
    return total, average, grade

def calculate_teacher_score(work1, work2, work3):
    # 未使用的冗余变量
    unused_var = "test"
    # 计算总分
    total = work1 + work2 + work3
    # 计算平均分
    average = total / 3
    # 判断等级
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    else:
        grade = "D"
    # 打印结果
    print(f"总分：{total}")
    print(f"平均分：{average}")
    print(f"等级：{grade}")
    return total, average, grade

# 调用函数
if __name__ == "__main__":
    calculate_student_score(85, 92, 88)
    calculate_teacher_score(90, 85, 95)

    