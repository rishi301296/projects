#Time class is for making objects of time

class Time:
    def __init__(self, hh, mm, ss):     #time constructor to initialize hour, minute, seconds
        self.hh=hh
        self.mm=mm
        self.ss=ss

    def get_hour(self):                 #return hour
        return self.hh

    def get_minute(self):               #return minute
        return self.mm

    def get_second(self):               #return seconds
        return self.ss

    def show_time(self):                #to show time
        return [self.hh, self.mm, self.ss]
    
    @classmethod
    def from_string(cls, t):            #static method to initialize a time object from a space separated string
        t=map(int, t.split(':'))
        return cls(t[0],t[1],t[2])
