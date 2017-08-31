import json
import os
from datetime import datetime
from Date import Date
from Time import Time

class Data:
    # to read the json file and save it in CHALLENGES, the json object
    def __init__(self):
        with open('ContestData.txt','r') as f:
            self.challenge=json.loads(f.read())
            f.close()
        self.validateData()

    # to compare a date with current date
    def compareDate(self, d, t):
        n=datetime.now()
        if d[2]>n.year:
            return 2
        elif d[2]<n.year:
            return 0
        else:
            if d[1]>n.month:
                return 2
            elif d[1]<n.month:
                return 0
            else:
                if d[0]>n.day:
                    return 2
                elif d[0]<n.day:
                    return 0
        return self.compareTime(t)

    # to compare time when date becomes equal
    def compareTime(self, t):
        n=datetime.now()
        if t[0]>n.hour:
            return 2
        elif t[0]<n.hour:
            return 0
        else:
            if t[1]>n.minute:
                return 2
            elif t[1]<n.minute:
                return 0
            else:
                if t[2]>n.second:
                    return 2
                elif t[2]<n.second:
                    return 0
        return 1

    # to validate update Upcoming and Ongoing contests
    def validateData(self):
        d=[]
        # validate contests of codechef
        for i in self.challenge['codechef']['Upcoming'].keys():
            x=self.compareDate(self.challenge['codechef']['Upcoming'][i]['start_date'],self.challenge['codechef']['Upcoming'][i]['start_time'])+self.compareDate(self.challenge['codechef']['Upcoming'][i]['end_date'],self.challenge['codechef']['Upcoming'][i]['end_time'])
            if x==0:
                del self.challenge['codechef']['Upcoming'][i]
            elif x<4:
                self.challenge['codechef']['Ongoing'][i]=self.challenge['codechef']['Upcoming'][i]
                del self.challenge['codechef']['Upcoming'][i]
        for i in self.challenge['codechef']['Ongoing'].keys():
            x=self.compareDate(self.challenge['codechef']['Ongoing'][i]['start_date'],self.challenge['codechef']['Ongoing'][i]['start_time'])+self.compareDate(self.challenge['codechef']['Ongoing'][i]['end_date'],self.challenge['codechef']['Ongoing'][i]['end_time'])
            if x==0:
                del self.challenge['codechef']['Ongoing'][i]

        # validate contests of hackerrank
        for i in self.challenge['hackerrank']['Upcoming'].keys():
            x=self.compareDate(self.challenge['hackerrank']['Upcoming'][i]['start_date'],self.challenge['hackerrank']['Upcoming'][i]['start_time'])+self.compareDate(self.challenge['hackerrank']['Upcoming'][i]['end_date'],self.challenge['hackerrank']['Upcoming'][i]['end_time'])
            if x==0:
                del self.challenge['hackerrank']['Upcoming'][i]
            elif x<4:
                self.challenge['hackerrank']['Ongoing'][i]=self.challenge['hackerrank']['Upcoming'][i]
                del self.challenge['hackerrank']['Upcoming'][i]
        for i in self.challenge['hackerrank']['Ongoing'].keys():
            x=self.compareDate(self.challenge['hackerrank']['Ongoing'][i]['start_date'],self.challenge['hackerrank']['Ongoing'][i]['start_time'])+self.compareDate(self.challenge['hackerrank']['Ongoing'][i]['end_date'],self.challenge['hackerrank']['Ongoing'][i]['end_time'])
            if x==0:
                del self.challenge['hackerrank']['Ongoing'][i]

    # to put the scrapped data into the json file
    def putData(self, site, code, name, start_date, start_time, end_date, end_time):
        start_date=[start_date.get_day(),start_date.get_month(),start_date.get_year()]
        start_time=[start_time.get_hour(),start_time.get_minute(),start_time.get_second()]
        end_date=[end_date.get_day(),end_date.get_month(),end_date.get_year()]
        end_time=[end_time.get_hour(),end_time.get_minute(),end_time.get_second()]
        x=self.compareDate(start_date, start_time)+self.compareDate(end_date, end_time)
        self.challenge[site][{0:'Over',1:'Ongoing',2:'Ongoing',3:'Ongoing',4:'Upcoming'}[x]][code]={
            'name' : name,
            'start_date' : start_date,
            'start_time' : start_time,
            'end_date' : end_date,
            'end_time' : end_time
            }
        with open("CD.txt","w") as f:
            f.write(json.dumps(self.challenge))
        f.close()
        os.remove("ContestData.txt")
        os.rename("CD.txt","ContestData.txt")

#d=Data()
#d.putData('codechef', 'hackcode55', 'Hack Code 55', Date.from_string('31 Aug 2019'), Time.from_string('21:30:00'), Date.from_string('31 Aug 2019'), Time.from_string('21:31:00'))
