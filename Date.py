#for making objects of date

class Date:
    def __init__(self, dd, mm, yy):         #date constructor to initialize date, month, year
        self.dd=dd
        try:
            self.mm={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}[mm]
        except:
            self.mm=int(mm)
        self.yy=yy

    def get_day(self):                     #return date
        return self.dd

    def get_month(self):                    #return month
        return self.mm

    def get_year(self):                     #return year
        return self.yy
    
    def show_date(self):                    # to return date as list
        return [self.dd,self.mm,self.yy]
    
    @classmethod
    def from_string(cls, d):                #static method to initialize a date object from a string
        c=' '
        if ':' in d:    c=':'
        elif '-' in d:  c='-'
        d=map(str, d.split(c))
        if len(d[2])==4:
            return cls(int(d[0]),d[1],int(d[2]))
        return cls(int(d[2]),d[1],int(d[0]))
