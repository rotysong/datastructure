def user():
    list = []
    f = open('user.txt')
    readlineTF = True
    while readlineTF:
        aa = f.readline()
        f.readline()
        bb = f.readline()
        ll = [aa.strip(), bb.strip()]
        list = list + ll
        if not f.readline():
            readlineTF = False

    return list


def word():
    f = open('word.txt')
    list = []
    readlineTF = True
    while readlineTF:
        aa = f.readline()
        f.readline()
        bb = f.readline()
        ll = [aa.strip(), bb.strip()]
        list = list + ll
        if not f.readline():
            readlineTF = False
    return list


class Adj:
    def __init__(self):
        self.n = 0
        self.next = None


class Vertex:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.n = 0
        self.first = None
        self.word=[]

    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

    def find(self, val):
        p = self.first
        while p is not None:
            if p.val == val:
                return p
            p = p.next
        return None

    def print(self):
        print(self.name, end=' ')
        print(self.nick)

    def vnick(self):
        a = []
        a.append(self.vnick)
        return a

    def vname(self):
        a = []
        a.append(self.name)
        return a


def multi(list):
    buf = list
    seen = []

    buf.sort()
    prev = buf[0]
    seen.append(buf[0])
    for i in range(1, len(buf)):
        if prev != buf[i]:
            prev = buf[i]
            seen.append(buf[i])
    return seen



def main():
    a = user()
    b = []
    c = 0
    d = 0
    cc = []
    dd = []
    ee = []
    ff = []
    dd2 = []
    ff2 = []

    for i in range(len(a)):
        j = i // 2
        if i % 2 == 0:
            b.append(Vertex(a[i], a[i + 1]))
    for i in range(len(b)):
        b[i].n = i

    f = open('friend.txt')
    readlineTF = True
    while readlineTF:
        aa = f.readline()
        bb = f.readline()
        cc = [aa.strip()]
        dd = dd + cc
        ee = [bb.strip()]
        ff = ff + ee

        if not f.readline():
            readlineTF = False

    for i in range(len(dd)):
        for j in range(len(b)):
            abc = b[j].vname()
            if dd[i] == abc[0]:
                dd2.append(Vertex(dd[i], b[j]))

    for i in range(len(ff)):
        for j in range(len(b)):
            abc = b[j].vname()
            if ff[i] == abc[0]:
                ff2.append(Vertex(ff[i], b[j]))

    for i in range(len(dd)):
        abcd = dd2[i].nick
        abce = ff2[i].nick
        abcd.add(abce)

    e = word()
    for i in range(len(e)):
        for j in range(len(b)):
            abc = b[j].vname()
            if e[i] == abc[0]:
                b[j].word = b[j].word+[i+1]


    return b

def total():
    count = 0
    a = word()
    b = main()
    c = []
    for i in range(len(a)-2):
        c.append(a[i])


    for i in range(5):
        p = b[i].first
        while p:
            p = p.next
            count += 1


    print("Total user: ", end = ' ')
    print(len(b))
    print("Total tweets: ", end = " ")
    print(len(c)//2)
    print("Total friendship records: ",end = "")
    print(count)

def mean():
    a = main()
    big = 0
    small = 0
    countt = 0

    ave = 0
    mit = 0
    mat = 0


    for i in range(len(a)):
        p = a[i].first
        count = 0
        while p:
            p = p.next
            count += 1
            countt+=1
        if count>big:
            big = count
        if count<small:
            small = count
    print('Average number of friends: ', end = '')
    print(countt//len(a))
    print('Minimum number of friends: ', end='')
    print(small)
    print('Maximum number of friends: ', end='')
    print(big)

    for i in range(len(a)):
        wordnumber = len(a[i].word)
        ave = ave + wordnumber
        if wordnumber > mat:
            mat = wordnumber
        if wordnumber < mit:
            mit = wordnumber


    print('Average tweets per friends: ', end='')
    print(ave // len(a))
    print('Minimum tweets per friends: ', end='')
    print(mit)
    print('Maximum tweets per friends: ', end='')
    print(mat)

def top5word():
    a = word()
    b = []
    c = []
    d = []
    e = []
    f = []
    g = []
    t5 = []

    for i in range(len(a)-2):
        if i%2 == 0:
            b.append(a[i])
        if i%2 == 1:
            c.append(a[i])
    c.sort()
    d = multi(c)

    for i in range(len(d)):
        count = 0
        for j in range(len(c)):
            if c[j] == d[i]:
                count +=1
        if count > 1:
            e.append(d[i])

    for i in range(len(e)):
        count = 0
        for j in range(len(c)):
         if e[i] == c[j]:
             count += 1
        if count > 0:
         f.append(count)

    g = list(f)
    f.sort()
    f.reverse()

    f = multi(f)
    f.reverse()

    count = 0

    for i in range(len(f)):
        if len(t5)<5:
            t5.append(f[i])

    for i in range(len(t5)):
     for j in range(len(g)):
        if  t5[i] == g[j] :
            t5[i] = e[i]

    for i in range(len(t5)):
        print(i+1, end='')
        print('번째', end = '')
        print(t5[i])
        
        

def userfind(str):
    a = main()
    b = word()
    m = 0
    for c in str:
        m = m + ord(c)
    m2 = 0

    user = []
    wd = []

    for i in range(5):
        p = a[i].first
        if p is not None:
         print(p.n)

    for i in range(len(b) - 2):
        if i % 2 == 0:
            user.append(b[i])
        if i % 2 == 1:
            wd.append(b[i])

    for i in range(len(wd)):
        for c in wd[i]:
            m2 = m2+ord(wd[i])
        if m2 == m:
            print(i)



total()
mean()
top5word()
userfind('그건')
