from datetime import datetime
import requests, statistics

class BangumiMark(object):
    def __init__(self, subnumber):
        self.subnumber = subnumber
        self.avgmark = 0
        self.standard_deviation = 0
        self.marklist = []
        #set a list to store each score is marked by how many people
        self.url = 'http://api.bgm.tv/subject/' + str(subnumber)
        r = requests.get(self.url)
        self.anime_dict = r.json()
        #use a dict to store serialized json data which is got from api
        r.close()

    def calculate(self):
        marksum = 0
        allmarklist = []
        marknumber = 1
        for i in range(1, 11):
            markrank = str(i)
            count = self.anime_dict['rating']['count'][markrank]
            #anime_dict['rating']['count'][markrank] stores the number of people marking 'i' score
            self.marklist.append(count)
            #then add the number into the list, pay attention that '1' is the first
            marksum = marksum + count * i
        self.avgmark = marksum / self.anime_dict['rating']['total']
        #anime_dict['rating']['total'] stores the number of people who have marked
        for peoplecount in self.marklist:
            if peoplecount != 0:
                for i in range(peoplecount):
                    allmarklist.append(marknumber)
            marknumber = marknumber + 1
        self.standard_deviation = statistics.stdev(allmarklist)

    def write_file(self):
        with open(r'C:\pythonworks\bangumimark\yurucampmarking.txt', 'a', encoding='utf-8') as f:
            f.write('原名：     %s\n' % self.anime_dict['name'])
            f.write('中文名：   %s\n' % self.anime_dict['name_cn'])
            f.write('评分：     %.4f\n' % self.avgmark)
            f.write('评分人数： %s\n' % self.anime_dict['rating']['total'])
            f.write('排名：     %s\n' % self.anime_dict['rank'])
            n = 1
            for voterank in self.marklist:
                f.write('打%s分人数：%s; ' % (n, voterank))
                n = n + 1
            f.write('\n标准差：   %.4f\n' % self.standard_deviation)
            updatetime = str(datetime.now())[:-7]
            f.write('更新时间： %s\n' % updatetime)
            f.write('--------------------------------------------\n')

BgmMark = BangumiMark(207195)
if BgmMark.anime_dict['type'] == 2:
    BgmMark.calculate()
    BgmMark.write_file()
