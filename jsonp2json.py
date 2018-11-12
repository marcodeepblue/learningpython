import re, json

def jsonp2json(jsonpobject):
    try:
        return json.loads(re.match(".*?({.*}).*", jsonpobject, re.S).group(1))
    except:
        raise ValueError('Invalid Input')
