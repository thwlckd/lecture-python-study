# hw6.2.py
# Program for class Student(Person)
# Author: 박창협
# Programed on October. 06. 2021

class Person:
    def __init__(self, name, age):
        self.setName(name)
        self.setAge(age)

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        if 0 <= age <= 150:
            self.age = age
        else:
            print("setAge Error! (out of age range 0~150) -> name: {}, age: {}".format(self.getName(), age))
            self.age = 0
        
    def __str__(self):
        return "Person({}, {}, {})".format(self.getName(), self.getReg_id(), self.getAge())

class Student(Person):
    def __init__(self, name, age, st_id, major, gpa):
        super().__init__(name, age)
        self.setSt_id(st_id)
        self.setMajor(major)
        self.setGPA(gpa)
    
    def getSt_id(self):
        return self.st_id

    def getMajor(self):
        return self.major

    def getGPA(self):
        return self.gpa

    def setSt_id(self, st_id):
        if 9999 < st_id < 100000:  # 학번 5자리로 설정
            self.st_id = st_id
        else:
            print("setSt_id Error! (out of st_id length 5) -> name: {}, st_id: {}".format(self.getName(), st_id))
            self.st_id = 0

    def setMajor(self, major):
        majors = {"EE", "ICE", "ME", "CE"}
        if major in majors:
            self.major = major
        else:
            print("setMajor Error! (undefined major) -> name: {}, major: {}".format(self.getName(), major))
            self.major = None

    def setGPA(self, gpa):
        if 0 <= gpa <= 4.5:
            self.gpa = gpa
        else:
            print("setGPA Error! (out of gpa range 0~4.5) -> name: {}, gpa: {}".format(self.getName(), gpa))
            self.gpa = 0

    def __str__(self):
        return "Student({}, {}, {}, {}, {})".format(self.getName(), self.getAge(), self.getSt_id(), self.getMajor(), self.getGPA())

def compareStudent(st1, st2, compare):
    if compare == "st_id":
        if st1.st_id < st2.st_id:
            return True
        else:
            return False
    if compare == "name":
        if st1.name < st2.name:
            return True
        else:
            return False
    if compare == "GPA":
        if st1.gpa > st2.gpa:  # decreasing order
            return True
        else:
            return False

def sortStudent(L_st, compare):
    for i in range(0, len(L_st)):
        min_idx = i
        for j in range(i+1, len(L_st)):
            if compareStudent(L_st[j], L_st[min_idx], compare):
                min_idx = j
        if min_idx != i:
            L_st[i], L_st[min_idx] = L_st[min_idx], L_st[i]

def printStudents(L_st):
    for s in range(len(L_st)):
        print(L_st[s])

# Application
if __name__ == "__main__":
    students = [
        Student("Kim", 21, 12345, "EE", 4.0),
        Student("Lee", 22, 11234, "ME", 4.2),
        Student("Park", 20, 10234, "ICE", 4.3),
        Student("Hong", 19, 13123, "CE", 4.1),
        Student("Yoon", 23, 11321, "ICE", 4.2)]

    print("students before sorting : ")
    printStudents(students)
    
    sortStudent(students, "name")
    print("\nstudents after sorting by name : ")
    printStudents(students)

    sortStudent(students, "st_id")
    print("\nstudents after sorting by student_id : ")
    printStudents(students)

    sortStudent(students, "GPA")
    print("\nstudents after sorting by GPA in decreasing order : ")
    printStudents(students)
