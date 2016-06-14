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

class Word:
    def __init__(self, name, word):
        self.name = name
        self.n = 0
        self.word = word
        self.first = None

    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

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

def wordlist():
    a = word()
    b = []
    c = []
    lword = []

    for i in range(len(a) - 2):
        if i % 2 == 0:
            b.append(a[i])
        if i % 2 == 1:
            c.append(a[i])

    for i in range(len(b)):
        lword.append(Word(b[i], c[i]))
        lword[i].n = i

    for i in range(len(lword)):
        for j in range(i + 1, len(lword), 1):
            if lword[i].name == lword[j].name:
                lword[i].add(lword[j])

    return lword

def wordlist2():
    a = wordlist()
    In = []
    In.append(a[0])
    p = a[0]

    for i in range(len(a)):
        if a[i].name != p.name:
            In.append(a[i])
            p = a[i]

    return In

def top5word(wordlist):
    a = wordlist
    userl = []
    wordl = []
    nomulti = []
    b = []
    rank = []
    orgrank = []
    top5 = []

    for i in range(len(a)):
        userl.append(a[i].name)
        wordl.append(a[i].word)

    nomulti = multi(wordl)

    for i in range(len(nomulti)):
        count = 0
        for j in range(len(wordl)):
            if nomulti[i] == wordl[j]:
                count += 1
        b.append((nomulti[i], count))

    for i in range(len(b)):
        rank.append(b[i][1])

    orgrank = list(rank)
    rank.sort()
    rank.reverse()
    top5.append(rank[0])
    prev = rank[0]
    i = 0
    while len(top5) < 5:
        if rank[i] != prev:
            top5.append(rank[i])
            prev = rank[i]
        i += 1
    for j in range(len(top5)):
        for i in range(len(b)):
            if b[i][1] == top5[j]:
                print(j + 1, end='')
                print("등: ", end='')
                print(b[i][0])

def top5user(wordlist, wordlist2):
    a = wordlist
    b = wordlist2
    tweetnumber = []
    rank = []
    top5 = []

    for i in range(len(b)):
        count = 0
        p = b[i].first
        count += 1
        while p is not None:
            p = p.next
            count += 1
        tweetnumber.append((b[i].name, count))

    for i in range(len(tweetnumber)):
        rank.append(tweetnumber[i][1])

    orgrank = list(rank)
    rank.sort()
    rank.reverse()
    top5.append(rank[0])
    prev = rank[0]
    i = 0
    while len(top5) < 5:
        if rank[i] != prev:
            top5.append(rank[i])
            prev = rank[i]
        i += 1
    for j in range(len(top5)):
        for i in range(len(tweetnumber)):
            if tweetnumber[i][1] == top5[j]:
                print(j + 1, end='')
                print("등: ", end='')
                print(tweetnumber[i][0])

def wordfind(string, wordlist, wordlist2):
    a = wordlist
    b = wordlist2
    tg = string
    list = []
    prev = 0
    for i in range(len(b)):
        p = b[i].first
        if b[i].word == tg:
            if b[i].name != prev:
                prev = b[i].name
                list.append(b[i].name)
        while p is not None:
            if a[p.n].word == tg:
                if a[p.n].name != prev:
                    prev = a[p.n].word
                    list.append(a[p.n].name)
            p = p.next
    return list

def meun():
    a = main()
    b = wordlist()
    c = wordlist2()
    count = 0
    count2 = 0
    print("select menu")
    print("1. Read data files")
    print("2. display statistics")
    print("3. Top 5 most tweeted words")
    print("4. Top 5 most tweeted users")
    print("5. Find users who tweeted a word")
    print("6. Find all people who are friends of the above users")
    print("7. Delete all mentions of a word")
    print("8. Delete all users who mentioned a word")
    print("9. Quit")
    number = 0
    while number != "9":
     number = input("메뉴 번호를 입력하세요")
     if number == "1":
         for i in range(len(a)):
             if a[i].name is not None:
                 count+=1
         for j in range(len(a)):
             p = a[j].first
             while p is not None:
                count2 +=1
                p = p.next
         print("Total user: ", end=' ')
         print(count)
         print("Total tweets: ", end=" ")
         print(len(b))
         print("Total friendship records: ", end="")
         print(count2)
     if number == "2":
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
                 countt += 1
             if count > big:
                 big = count
             if count < small:
                 small = count
         print('Average number of friends: ', end='')
         print(countt // len(a))
         print('Minimum number of friends: ', end='')
         print(small)
         print('Maximum number of friends: ', end='')
         print(big)

         for i in range(len(c)):
             countt = 0
             p = b[i].first
             countt += 1
             while p is not None:
                 p = p.next
                 countt += 1
             if countt > mat:
                 mat = countt
             if countt < mit:
                 mit = countt

         print('Average tweets per users: ', end='')
         print(len(b) // len(a))
         print('Minimum tweets per users: ', end='')
         print(mit)
         print('Maximum tweets per users: ', end='')
         print(mat)
     if number == "3":
        top5word(b)
     if number == "4":
        top5user(b, c)
     if number == "5":
        string = input("단어를 입력하세요")
        list = wordfind(string, b,c)
        print(list)
     if number == "6":
        string = input("단어를 입력하세요")
        list6 = wordfind(string, b,c)
        for i in range(len(list6)):
            for j in range(len(a)):
                p = a[j].first
                if list6[i] == a[j].name:
                    print(list6[i], end='')
                    print('의 친구들', end='')
                    while p is not None:
                        print(a[p.n].name, end='')
                        print(", ", end='')
                        p = p.next
            print(' ')
     if number == "7":
        string = input("지우고 싶은 단어를 입력하세요")
        tg = string
        prev = 0
        for i in range(len(c)):
         prev = c[i]
         p = c[i].first
         if c[i].word == tg:
             c[i] = c[i].first
         while p is not None:
             if b[p.n].word == tg:
                 prev.next = p.next
             prev = p
             p = p.next
     if number == "8":
        string = input("단어를 입력하세요")
        Flist = wordfind(string, b, c)
        for i in range(len(Flist)):
            for j in range(len(a)):
                prev = a[j]
                p = a[j].first
                if Flist[i] == a[j].name:
                    a[j] = a[j].first
                if Flist[i] == a[p.n].name:
                    a[j].first = p.next
                    prev = p
                    p = p.next
                while p is not None:
                    if Flist[i] == a[p.n].name:
                        prev.next = p.next
                    prev = p
                    p = p.next

        for i in range(len(Flist)):
            for j in range(len(a)):
                if Flist[i] == a[j].name:
                    a[j].name = None
                    a[j].nick = None
                    a[j].n = 0
                    a[j].first = None
                    a[j].word = []
     if number == "9":
        return print("감사합니다")


meun()
