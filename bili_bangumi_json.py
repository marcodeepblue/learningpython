import re
import requests
import json

r = requests.get('http://bangumi.bilibili.com/jsonp/seasoninfo/25696.ver?callback=seasonListCallback')
jsonp_text = r.text
def jsonp2json(jsonpobject):
    try:
        return json.loads(re.match(".*?({.*}).*", jsonpobject, re.S).group(1))
    except:
        raise ValueError('Invalid Input')

json_text = jsonp2json(jsonp_text)
a = json_text['result']['season_status']
b = json_text['result']['title']
c = json_text['result']['play_count']
d = json_text['result']['favorites']
print(a, b, c, d)