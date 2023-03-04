# hw6.4.py
# Program for class Time
# Author: 박창협
# Programed on October. 06. 2021

class Time:
    def __init__(self, hr, mn, sec):
        self.setHour(hr)
        self.setMinute(mn)
        self.setSecond(sec)
    def __lt__(self, other):
        if (self.hour, self.minute, self.second) < (other.hour, other.minute, other.second):
            return True
        else:
            return False

    def __str__(self):
        return "({:02d}:{:02d}:{:02d})".format(self.getHour(), self.getMinute(), self.getSecond())

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute
    
    def getSecond(self):
        return self.second

    def setHour(self, hour):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            print("setHour Error! (out of hour range 0~23) -> hour: {}".format(hour))
            self.hour = 0

    def setMinute(self, minute):
        if 0 <= minute <= 59:
            self.minute = minute
        else:
            print("setMinute Error! (out of minute range 0~59) -> minute: {}".format(minute))
            self.minute = 0
        
    def setSecond(self, second):
        if 0 <= second <= 59:
            self.second = second
        else:
            print("setSecond Error! (out of second range 0~59) -> second: {}".format(second))
            self.second = 0

# Application
times = [
    Time(23, 59, 59),
    Time(9, 0, 5),
    Time(13, 30, 0),
    Time(3, 59, 59),
    Time(0, 0, 0),]

print("times before sorting : ")
for t in times:
    print(t)

times.sort()
print("\ntimes after sorting : ")
for t in times:
    print(t)
