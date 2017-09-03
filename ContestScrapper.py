import re
import urllib2 as U
from BeautifulSoup import BeautifulSoup as B
from Time import Time
from Date import Date
from Data import Data

global data_obj

class Contest:
    def __init__(self):
        self.codechefUrl="https://www.codechef.com/contests"
        self.hackerrankUrl="https://www.hackerrank.com/contests"
        self.codeforcesUrl="http://codeforces.com/api/contest.list"
        self.hackerearthUrl=""
    
    def getContentOfCodechef(self):
        try:
            h=U.urlopen(self.codechefUrl)
            s=''.join(_ for _ in h.readlines())
            x=B(s)
            p=x('table', {'class':'dataTable'})[0]('td')
            for i in xrange(0,len(p),4):
                data_objputData('codechef', p[i].text, p[i+1]('a')[0].text, Date.from_string(p[i+2].contents[0]), Time.from_string(p[i+2].contents[2]),Date.from_string(p[i+3].contents[0]),Time.from_string(p[i+3].contents[2]))
            p=x('table', {'class':'dataTable'})[1]('td')
            for i in xrange(0,len(p),4):
                data_obj.putData('codechef', p[i].text, p[i+1]('a')[0].text, Date.from_string(p[i+2].contents[0]), Time.from_string(p[i+2].contents[2]),Date.from_string(p[i+3].contents[0]),Time.from_string(p[i+3].contents[2]))
        except:
            print '502 Codechef not available!!!'

    def getContentOfHackerrank(self):
        try:
            h=U.urlopen(self.hackerrankUrl)
            s=''.join(_ for _ in h.readlines())
            x=B(s)
            p=x('ul', {'class':'contests-active'})[0]('li')

            for i in xrange(1,len(p)):
                sdt=map(str, p[i]('div')[0]('div')[1].find('meta', {'itemprop':'startDate'})['content'].split('.'))[0]
                edt=map(str, p[i]('div')[0]('div')[1].find('meta', {'itemprop':'endDate'})['content'].split('.'))[0]
                sd, st = map(str, sdt.split('T'))
                ed, et = map(str, edt.split('T'))

                data_obj.putData('hackerrank', p[i].find('div')['data-slug'], p[i]('div')[0]('div')[0].text, Date.from_string(sd), Time.from_string(st),Date.from_string(ed),Time.from_string(et))
        except:
            print '502 Hackerrank not available!!!'

    def getContentOfCodeforces(self):
        try:
            h=U.urlopen(self.codeforcesUrl)
            s=''.join(_ for _ in h.readlines())
            print s[:1000]
        except:
            print '502 Codeforces not available!!!'

data_obj=Data()
c=Contest()
#c.getContentOfCodechef()
#c.getContentOfHackerrank()
c.getContentOfCodeforces()
