import json
import os
from datetime import datetime
from Date import Date
from Time import Time

class Data:
    def __init__(self):
        with open('ContestData.txt','r') as f:
            self.challenge=json.loads(f.read())
            f.close()
        for i in self.challenge['codechef']['Upcoming']:

    def compareDate(self, d):
        n=datetime.now()
        if d.get_year()>n.year:
            return 2
        elif d.get_year()<n.year:
            return 0
        else:
            if d.get_month>n.month:
                return 2
            elif d.get_month<n.month:
                return 0
            else:
                if d.get_date>n.day:
                    return 2
                elif d.get_date<n.day:
                    return 0
        return 1

    def putData(self, site, code, name, start_date, start_time, end_date, end_time):
        self.challenge[site][{0:'Over',1:'Ongoing',2:'Upcoming'}[self.compareDate(start_date)]][code]={
            'name' : name,
            'start_date' : start_date.show_date(),
            'start_time' : start_time.show_time(),
            'end_date' : end_date.show_date(),
            'end_time' : end_time.show_time()
            }
        with open("CD.txt","w") as f:
            f.write(json.dumps(self.challenge))
        os.remove("ContestData.txt")
        os.rename("CD.txt","ContestData.txt")

d=Data()
d.putData('codechef', 'hackcode3', 'Hack Code 3', Date.from_string('28 Jan 2018'), Time.from_string('10:10:10'), Date.from_string('29 Jan 2018'), Time.from_string('11:10:10'))
