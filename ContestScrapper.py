import re
import urllib2 as U
from BeautifulSoup import BeautifulSoup as B
from Time import Time
from Date import Date

class Challange:
    def __init__(self, code, name, start_date, start_time, end_date, end_time):
        self.code=code
        self.name=name
        self.start_date=start_date
        self.start_time=start_time
        self.end_date=end_date
        self.end_time=end_time

class Contest:
    def __init__(self):
        self.codechef={'Ongoing':[],'Upcoming':[]}
        self.codechefUrl="https://www.codechef.com/contests"
        self.hackerrank={'Ongoing':[],'Upcoming':[]}
        self.hackerrankUrl="https://www.hackerrank.com/contests"
        self.codeforces={'Ongoing':[],'Upcoming':[]}
        self.codeforcesUrl=""
        self.hackerearth={'Ongoing':[],'Upcoming':[]}
        self.hackerearthUrl=""
    
    def getContentOfCodechef(self):
        try:
            h=U.urlopen(self.codechefUrl)
            s=''.join(_ for _ in h.readlines())
            x=B(s)
            p=x('table', {'class':'dataTable'})[0]('td')
            for i in xrange(0,len(p),4):
                chal=Challange(p[i].text,p[i+1]('a')[0].text,Date.from_string(p[i+2].contents[0]),Time.from_string(p[i+2].contents[2]),Date.from_string(p[i+3].contents[0]),Time.from_string(p[i+3].contents[2]))
                self.codechef['Ongoing'].append(chal)
            p=x('table', {'class':'dataTable'})[1]('td')
            for i in xrange(0,len(p),4):
                chal=Challange(p[i].text,p[i+1]('a')[0].text,Date.from_string(p[i+2].contents[0]),Time.from_string(p[i+2].contents[2]),Date.from_string(p[i+3].contents[0]),Time.from_string(p[i+3].contents[2]))
                self.codechef['Upcoming'].append(chal)
        except:
            print '404 Codechef not available!!!'

    def getContentOfHackerrank(self):
        try:
            h=U.urlopen(self.hackerrankUrl)
            s=''.join(_ for _ in h.readlines())
            x=B(s)
            p=x('ul', {'class':'contests-active'})[0]('li')

            print p[0]('div')[0]
            print ''
            print p[1]
            print ''
            print p[2]
            #re.search(r'data-slug="(\w+)"',str(p[0]))
            
            '''
            for i in xrange(4,len(p),4):
                print p[i]('div')
                print p[i+1].text
                print ''
            '''
            '''
            for i in xrange(0,len(p),4):
                sd=p[i+2].contents[0].split()
                chal=challange(p[i].text,p[i+1]('a')[0].text,date(sd[0],sd[1],sd[2]),p[i+2].contents[2],p[i+3].contents[0],p[i+3].contents[2])
                codechef['Ongoing'].append(chal)
            p=x('table', {'class':'dataTable'})[1]('td')
            for i in xrange(0,len(p),4):
                chal=challange(p[i].text,p[i+1]('a')[0].text,p[i+2].contents[0],p[i+2].contents[2],p[i+3].contents[0],p[i+3].contents[2])
                codechef['Will Start'].append(chal)'''
        except:
            print '404 Hackerrank not available!!!'

c=Contest()
c.getContentOfCodechef()
#c.getContentOfHackerrank()


for i in c.codechef['Upcoming']:
    print i.code
    print i.name
    print i.start_date.show_date()
    print i.start_time.show_time()
    print i.end_date.show_date()
    print i.end_time.show_time()
    print ''

