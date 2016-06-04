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

    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

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

    f = open('2.txt')
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

    return b

def total():
    count = 0
    a = word()
    b = main()
    c = []
    for i in range(len(a)-2):
        c.append(a[i])


    for i in range(5):
        print(b[i].name)
        p = b[i].first
        while p:
            print(b[p.n].name)
            p = p.next
            count += 1
        print('------')

    print("Total user: ", end = ' ')
    print(len(b))
    print("Total tweets: ", end = " ")
    print(len(c)//2)
    print("Total friendship records: ",end = "")
    print(count)






total()
