#Date class is for making objects of date

class Date:
    def __init__(self, dd, mm, yy):         #date constructor to initialize date, month, year
        self.dd=dd
        self.mm={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}[mm]
        self.yy=yy

    def show_date(self):                    # to show date
        return [self.dd,self.mm,self.yy]
    
    @classmethod
    def from_string(cls, d):                #static method to initialize a date object from a string
        d=map(str, d.split())
        return cls(int(d[0]),d[1],int(d[2]))
