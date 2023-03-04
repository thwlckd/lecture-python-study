# hw6.1.py
# Program for class Person
# Author: 박창협
# Programed on October. 06. 2021

class Person:
    def __init__(self, name, reg_id, age):
        self.setName(name)
        self.setReg_id(reg_id)
        self.setAge(age)

    def getName(self):
        return self.name

    def getReg_id(self):
        return self.reg_id

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

    def setReg_id(self, reg_id):
        if reg_id < 1000000:  # 주민번호 앞 6자리
            self.reg_id = reg_id
        else:
            print("setReg_id Error! (out of reg_id length 6) -> name: {}, reg_id: {}".format(self.getName(), reg_id))
            self.reg_id = 0

    def setAge(self, age):
        if 0 <= age <= 150:
            self.age = age
        else:
            print("setAge Error! (out of age range 0~150) -> name: {}, age: {}".format(self.getName(), age))
            self.age = 0
        
    def __str__(self):
        return "Person({}, {}, {})".format(self.getName(), self.getReg_id(), self.getAge())

def printPersonList(L_persons):
    for p in L_persons:
        print(" ", p)

# Application
if __name__ == "__main__":
    persons = [
        Person("Kim", 990101, 21),
        Person("Lee", 980715, 22),
        Person("Park", 101225, 20),
        Person("Hong", 110315, 19),
        Person("Yoon", 971005, 23),
        Person("Wrong", 100000, 350)] 
    print("persons : ")
    printPersonList(persons)
