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
        self.word = []

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
                b[j].word = b[j].word + [i + 1]

    return b


def total():
    count = 0
    a = word()
    b = main()
    c = []
    for i in range(len(a) - 2):
        c.append(a[i])

    for i in range(5):
        p = b[i].first
        while p:
            p = p.next
            count += 1

    print("Total user: ", end=' ')
    print(len(b))
    print("Total tweets: ", end=" ")
    print(len(c) // 2)
    print("Total friendship records: ", end="")
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
    userl = []
    wordl = []
    nomulti = []
    b = []
    rank = []
    orgrank = []
    top5 = []

    for i in range(len(a) - 2):
        if i % 2 == 0:
            userl.append(a[i])
        if i % 2 == 1:
            wordl.append(a[i])

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


def top5user():
    a = wordlist()
    b = wordlist2()
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


def wordfind(string):
    a = wordlist()
    b = wordlist2()
    tg = string
    list = []
    prev = 0
    for i in range(len(b)):
        p = b[i].first
        while p is not None:
            if b[i].word == tg:
                if b[i].name != prev:
                    prev = b[i].name
                    list.append(b[i].name)
            if a[p.n].word == tg:
                if a[p.n].name != prev:
                    prev = a[p.n].word
                    list.append(a[p.n].name)
            p = p.next

    print(list)


def wordfind2(string):
    a = wordlist()
    b = wordlist2()
    tg = string
    list = []
    prev = 0
    for i in range(len(b)):
        p = b[i].first
        while p is not None:
            if b[i].word == tg:
                if b[i].name != prev:
                    prev = b[i].name
                    list.append(b[i].name)
            if a[p.n].word == tg:
                if a[p.n].name != prev:
                    prev = a[p.n].word
                    list.append(a[p.n].name)
            p = p.next

    return list


def wordfriend(string):
    a = main()
    b = wordfind2(string)
    for i in range(len(b)):
        for j in range(len(a)):
            p = a[j].first
            if b[i] == a[j].name:
                print(b[i],end = '')
                print('의 친구들',end = '')
                while p is not None:
                    print(a[p.n].name, end = '')
                    print(", ", end = '')
                    p = p.next
            print(' ')


def wordfriend2(string):
    a = main()
    b = wordfind2(string)
    list = []
    for i in range(len(b)):
        for j in range(len(a)):
            p = a[j].first
            if b[i] == a[j].name:
                while p is not None:
                    list.append((a[p.n].name))
                    p = p.next
    return list


def worddelete(string):
    a = wordlist()
    b = wordlist2()
    tg = string
    prev = 0
    for i in range(len(b)):
        prev = b[i]
        p = b[i].first
        if b[i].word == tg:
            b[i] = b[i].first
        if a[p.n].word == tg:
            b[i].first = p.next
            prev = p
            p = p.next
        while p is not None:
            if a[p.n].word == tg:
                prev.next = p.next
            prev = p
            p = p.next


def frienddelete(string):
    Flist = wordfriend2(string)
    a = main()
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


def meun():
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

    number = input("메뉴 번호를 입력하세요")
    if number == 1:
        total()
    if number == 2:
        mean()
    if number == 3:
        top5user()
    if number == 4:
        top5word()
    if number == 5:
        string = input("찾고 싶은 단어를 입력하세요")
        wordfind(string)
    if number == 6:
        string = input("찾고 싶은 친구가 입력한 단어를 입력하세요")
        wordfind(string)
        wordfriend(string)
    if number == 7:
        string = input("지우고 싶은 단어를 입력하세요")
        worddelete(string)
    if number == 8:
        string = input("단어를 입력하세요")
        frienddelete(string)
    if number == 9:
        return print("감사합니다")
    else:
        return print("잘못입력하셨습니다. 다시 실행하세요")


meun()
