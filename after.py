# 重构后的优质代码
def calculate_score(a, b, c):
    total = a + b + c
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
    calculate_score(85, 92, 88)
    calculate_score(90, 85, 95)