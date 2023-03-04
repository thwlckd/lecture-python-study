# hw7.2.py
# Program for using student_records.txt
# Author: 박창협
# Programed on October. 11. 2021

def calculate_scroe(data_list):
    i = 0
    for name, st_id, kor, eng, math, sci in data_list:
        sum = kor + eng + math + sci
        data_list[i].append(sum)
        data_list[i].append(sum/4)
        i = i + 1

def fwrite_data(file_name, data_list):
    f = open(file_name, 'w', encoding = "utf-8")
    f.write("name\t st_id\t   kor\t eng  math  sci  sum   avg\n")
    f.write("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐-----------------\n")
    for data in data_list:
        s = "{}\t".format(data[0])
        s += "{}   ".format(data[1])
        s += "{}\t ".format(data[2])
        s += "{}    ".format(data[3])
        s += "{}   ".format(data[4])
        s += "{:}    ".format((data[5]))
        s += "{:}   ".format((data[6]))
        s += "{:.2f}".format(float(data[7]))
        s += '\n'
        f.write(s)
    f.close()

def print_data(data_list):
    print("name\t st_id\t   kor\t eng  math  sci  sum   avg\n")
    print("‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐------------------\n")
    for data in data_list:
        s = "{}\t".format(data[0])
        s += "{}   ".format(data[1])
        s += "{}\t ".format(data[2])
        s += "{}    ".format(data[3])
        s += "{}   ".format(data[4])
        s += "{:}    ".format((data[5]))
        s += "{:}   ".format((data[6]))
        s += "{:.2f}".format(float(data[7]))
        s += '\n'
        print(s)

# main
students = []
file_path = "C:/Users/박창협/Desktop/과제/파이썬프로그래밍과응용/py/hw7/student_records.txt"
f = open(file_path, 'r')
for line in f.readlines():
    name, st_id, kor, eng, math, sci = line.split()
    students.append([name, int(st_id), int(kor), int(eng), int(math), int(sci)])

for i in students:
    print(i)

calculate_scroe(students)
print_file_path = "C:/Users/박창협/Desktop/과제/파이썬프로그래밍과응용/py/hw7/output.txt"
print("\nAfter statistics analysis")
fwrite_data(print_file_path, students)
print_data(students)

kor_sum = 0
eng_sum = 0
math_sum = 0
sci_sum = 0
num_students = len(students)
for i in students:
    kor_sum += i[2]
    eng_sum += i[3]
    math_sum += i[4]
    sci_sum += i[5]

print("Average score of each class:")
print("kor_avg =", kor_sum/num_students)
print("eng_avg =", eng_sum/num_students)
print("math_avg =", math_sum/num_students)
print("sci_avg =", sci_sum/num_students)
