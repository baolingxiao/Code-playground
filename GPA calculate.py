# 学生成绩字典
grades = {}

# 添加成绩
def add_grade(student, course, grade, credits):
    if student in grades:
        grades[student].append((course, grade, credits))
    else:
        grades[student] = [(course, grade, credits)]

# 计算 GPA
def calculate_gpa(student):
    if student in grades:
        total_points = sum(grade * credits for course, grade, credits in grades[student])
        total_credits = sum(credits for course, grade, credits in grades[student])
        gpa = total_points / total_credits
        return gpa
    else:
        return None


# 百分制转 GPA
def percentage_to_gpa(percentage):
    if percentage >= 90:
        return 4.0
    elif percentage >= 85:
        return 3.7
    elif percentage >= 80:
        return 3.3
    elif percentage >= 75:
        return 3.0
    elif percentage >= 70:
        return 2.7
    elif percentage >= 65:
        return 2.3
    elif percentage >= 60:
        return 2.0
    elif percentage >= 55:
        return 1.7
    elif percentage >= 50:
        return 1.3
    elif percentage >= 45:
        return 1.0
    else:
        return 0.0


    
#学生信息

def input_grades():
    while True:
        student = input("Enter student name (or type 'stop' to finish): ")
        if student.lower() == 'stop':
            break
        course = input("Enter course name: ")
        percentage = float(input("Enter grade percentage: "))
        grade = percentage_to_gpa(percentage)
        credits = float(input("Enter credits: "))
        add_grade(student, course, grade, credits)

input_grades()

print("GPA Calculation")

for student in grades:
    print(f"{student}'s GPA:{calculate_gpa(student):.2f}")
