# hw6.3.py
# Program for class Date
# Author: 박창협
# Programed on October. 06. 2021

class Date:
    def __init__(self, yr, mt, dy):
        self.setYear(yr)
        self.setMonth(mt)
        self.setDay(dy)

    def __lt__(self, other):
        if (self.year, self.month, self.day) < (other.year, other.month, other.day):
            return True
        else:
            return False

    def __str__(self):
        return "Date({:>4}‐{:>02d}‐{:>02d})".format(self.getYear(), self.getMonth(), self.getDay())

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def setYear(self, year):
        self.year = year
        
    def setMonth(self, month):
        if 1 <= month <= 12:
            self.month = month
        else:
            print("setMonth Error! (out of year range 1~12) -> month: {}".format(month))
            self.month = 1

    def isLeapYear(self, year):
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            return True
        else:
            return False

    def setDay(self, day):
        daysOfMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.isLeapYear(self.year):
            daysOfMonth[2] = 29
        if 1 <= day <= daysOfMonth[self.month]:
            self.day = day
        else:
            print("setDay Error! (out of year range 1~31) -> ({}-{}-{})".format(self.year, self.month, day))
            self.day = 1
    
# Application
if __name__ == "__main__":
    dates = [
        Date(2000, 9, 15),
        Date(1997, 2, 20),
        Date(2001, 5, 2),
        Date(2001, 5, 1),
        Date(1999, 3, 1)]
    
    print("dates before sorting : ")
    for d in dates:
        print(d)

    dates.sort()
    print("\ndates after sorting : ")
    for d in dates:
        print(d)
