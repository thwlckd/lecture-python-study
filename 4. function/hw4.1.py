# hw4.1.py
# 학생들이 성적분포를 계산하는 프로그램
# Author: 박창협
# Programed on September. 27. 2021

def statistics_student_GPA(L_student):
    L_GPAs=[]
    sum = 0
    print("students :")
    for i in L_student:
        L_GPAs.append(i[4])
        sum += i[4]
        print(i)

    avg = sum / len(L_student)
    max_GPA = max(L_GPAs)
    min_GPA = min(L_GPAs)
    print("statistics_student_GPA:")
    print(" - L_GPAs = {}\n - num_students = {}\n\
 - Statistics of GPAs : Max({}), Min({}), Avg({})".format(L_GPAs, len(L_student), max_GPA, min_GPA, avg))


students = [
    ('Kim', 'EE', 12345, (2000, 12, 25), 4.0),
    ('Lee', 'ME', 11234, (2019, 9, 1), 4.2),
    ('Park', 'ICE', 10234, (2019, 3, 1), 4.3),
    ('Hong', 'CE', 13123, (2021, 1, 1), 4.1),
    ('Yoon', 'ICE', 11321, (2001, 8, 15), 4.2),
    ('A', 'ICE', 12321, (2000, 7, 31), 4.2)]

statistics_student_GPA(students)
