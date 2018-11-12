from datetime import datetime
import requests, time

for urlnumber in range(239815, 239817):
    url = 'http://api.bgm.tv/subject/' + str(urlnumber)
    r = requests.get(url)
    anime_dict = r.json()
    marksum = 0
    #because the score API supplied is not accurate enough
    #use a loop to calculate the summary of the scores, then divide the number of people
    marklist = []
    #set a list to store each score(1, 2, 3..., 10) is marked bu how many people
    if anime_dict['type'] == 2:
        for i in range(1, 11):
            markrank = str(i)
            count = anime_dict['rating']['count'][markrank]
            marklist.append(count)
            marksum = marksum + count * i
        avgmark = marksum / anime_dict['rating']['total']
        with open(r'C:\pythonworks\bangumimark\animemarking.txt', 'a') as f:
            f.write('原名：     %s\n' % anime_dict['name'])
            f.write('中文名：   %s\n' % anime_dict['name_cn'])
            f.write('评分：     %.4f\n' % avgmark)
            f.write('评分人数： %s\n' % anime_dict['rating']['total'])
            n = 1
            for voterank in marklist:
                f.write('打%s分人数：%s; ' % (n, voterank))
                n = n + 1
            f.write('\n排名：     %s\n' % anime_dict['rank'])
            f.write('更新时间： %s\n' % datetime.now())
            f.write('--------------------------------------------\n')
    time.sleep(30)
with open(r'C:\pythonworks\bangumimark\animemarking.txt', 'a') as f:
    f.write('---------------------本次更新结束---------------------\n')