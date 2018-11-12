import re
class DeepBlueAdmin(object):
    def __init__(self, username, password):
        lenuser = len(username)
        lenpass = len(password)
        if lenuser < 4 or lenuser > 16:
            raise ValueError('The length of username must be between 4 and 16')
        elif lenpass < 6 or lenpass > 16:
            raise ValueError('The length of password must be between 6 and 16')
        if not re.match(r'[a-zA-Z][0-9a-zA-Z]+', username):
            raise ValueError('Username must be made up of numbers and letters, and first character must be a letter')
        if not re.match(r'[a-zA-Z][0-9a-zA-Z]+', password):
            raise ValueError('Password must be made up of numbers and letters, and first character must be a letter')
        self.username = username
        self.password = password

class DeepBlueTranslator(object):
    def __init__(self, context):
        self.context = context
        self.dict_translate = {'aa': 'bb', 'cc': 'dd', 'eee':'fff', 'g':'h', 'iiii':'jjjj', 'kk': 'll'}
        self.listOriginal = self.context.split()
        self.listEnd = []
    def trans_word(self):
        for word in self.listOriginal:
            if word in self.dict_translate:
                self.listEnd.append(self.dict_translate[word])
            else:
                self.listEnd.append('???')
    def print_out(self):
        a = ''
        self.listingword()
        self.trans_word()
        for t_words in self.listEnd:
            a = a + t_words
            a = a + ' '
        s = len(a)
        a = a[:(s-1)]
        print(a)

class DeepBlueCrossingRoad(object):
    def __init__(self, roadwidth, peopledetail=Adult):
        self.roadwidth = roadwidth
        self.peopledetail = peopledetail
        self.accessible = False
        self.speed = 0
        self.time = 0
    def crossingspeed(self):
        if self.peopledetail == Adult:
            self.speed = 1.1
        elif self.peopledetail == Elder:
            self.speed = 0.8
        elif self.peopledetail == Children:
            self.speed = 1
        else:
            raise AttributeError('people detail must be Adult, Elder or Children')
        return self.speed
    def crossingtime(self):
        self.time = rodawith / self.crossingspeed()
        return self.time
    def safe(self):
        if self.crossingtime() > 30:
            print('Not safe')
        else:
            print('Safe')