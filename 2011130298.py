def user():
    list = []
    f = open('user2.txt')
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
    f = open('word2.txt')
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
        self.word = []
        self.n = 0
        self.first = None

    def add(self, v):
        a = Adj()
        a.n = v.n
        a.next = self.first
        self.first = a

    def addword(self,word):
        self.word.append(word)

    def delword(self,word):
        self.word.remove(word)

class Word:
    def __init__(self,word):
        self.word = word
        self.people = []

    def add(self, v):
        self.people.append(v)

    def delete(self,v):
        self.people.remove(v)

def hash(str):
    m = 0
    for c in str:
        m = m + ord(c)
    return m

def wordlist():
        lword = word()
        list = []
        list2 = []
        hlist = []
        origin = []
        m = 0
        j = 0

        for i in range(len(lword) - 2):
            if i % 2 == 0:
                list2.append((lword[i], lword[i + 1]))

        for i in range(len(list2)):
            m = hash(list2[i][1])
            hlist.append(m)

        origin = hlist[:]
        hlist.sort()
        hlist = multi(hlist)

        for i in range(len(hlist)):
            m = 0
            j = 0
            while m != 1:
                if hlist[i] == origin[j]:
                    list.append(Word(list2[j][1]))
                    m = 1
                else:
                    j += 1

        for i in range(len(list)):
            for j in range(len(list2)):
                if list[i].word == list2[j][1]:
                    list[i].add(list2[j][0])

        return list

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
    Vlist = []
    cc = []
    dd = []
    follower = []
    follower2 = []
    followee = []
    followee2 = []

    for i in range(len(a)):
        j = i // 2
        if i % 2 == 0:
            Vlist.append(Vertex(a[i], a[i + 1]))
    for i in range(len(Vlist)):
        Vlist[i].n = i

    f = open('friend2.txt')
    readlineTF = True
    while readlineTF:
        aa = f.readline()
        bb = f.readline()
        cc = [aa.strip()]
        dd = [bb.strip()]
        follower = follower+cc
        followee = followee+dd

        if not f.readline():
            readlineTF = False

    for i in range(len(follower)):
        for j in range(len(Vlist)):
            if follower[i] == Vlist[j].name:
                follower2.append((follower[i],Vlist[j]))

    for i in range(len(followee)):
        for j in range(len(Vlist)):
            if followee[i] == Vlist[j].name:
                followee2.append((followee[i],Vlist[j]))

    for i in range(len(follower2)):
        follower2[i][1].add(followee2[i][1])

    lword = word()
    wordl = []
    for i in range(len(lword)):
        if i%2 == 0:
            wordl.append((lword[i],lword[i+1]))

    for i in range(len(Vlist)):
      for j in range(len(wordl)):
        if Vlist[i].name == wordl[j][0]:
            Vlist[i].addword(wordl[j][1])

    return Vlist

def top5word(word_list):
    word = word_list
    usernumber = []
    origin = []
    top5number = []
    for i in range(len(word)):
        usernumber.append(len(word[i].people))
    origin = usernumber[:]
    usernumber.sort()
    usernumber = multi(usernumber)
    usernumber.reverse()

    for i in range(5):
        for j in range(len(word)):
            if origin[j] == usernumber[i]:
                print(i+1, end = '')
                print("등 단어 :", end = '')
                print(word[j].word)

def top5user(user_list):
    user = user_list
    list = []
    org = []
    for i in range(len(user)):
        list.append(len(user[i].word))
    org = list[:]
    list.sort()
    list = multi(list)
    list.reverse()

    for i in range(5):
        for j in range(len(org)):
            if org[j] == list[i]:
                print(i+1, end = '')
                print("등 user :", end = '')
                print(user[j].name)

def menu():
        a = main()
        b = wordlist()
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
        deletedword = []
        deleteduser = []
        while number != "9":
            number = input("메뉴 번호를 입력하세요")
            if number == "1":
                count = 0
                for j in range(len(a)):
                    p = a[j].first
                    while p is not None:
                        count += 1
                        p = p.next
                print("Total user: ", end=' ')
                print(len(a))
                print("Total tweets: ", end=" ")
                print(len(b))
                print("Total friendship records: ", end="")
                print(count)
            if number == "2":
                count = 0
                countfriend = 0
                minfriend = 0
                maxfriend = 0
                counttweet = 0
                mintweet = 0
                maxtweet = 0
                for j in range(len(a)):
                    countfriend = 0
                    counttweet = len(a[j].word)
                    p = a[j].first
                    while p is not None:
                        count +=1
                        countfriend +=1
                        p = p.next
                    if minfriend > countfriend:
                        minfriend = countfriend
                    if maxfriend < countfriend:
                        maxfriend = countfriend
                    if mintweet > counttweet:
                        mintweet = counttweet
                    if maxtweet < counttweet:
                        maxtweet = counttweet
                print('Average number of friends: ', end='')
                print(count//len(a))
                print('Minimum number of friends: ', end='')
                print(minfriend)
                print('Maximum number of friends: ', end='')
                print(maxfriend)
                print('Average tweets per users: ', end='')
                print(len(b)//len(a))
                print('Minimum tweets per users: ', end='')
                print(mintweet)
                print('Maximum tweets per users: ', end='')
                print(maxtweet)
            if number == "3":
                top5word(b)
            if number == "4":
                top5user(a)
            if number == "5":
                string = input("단어를 입력하세요")
                for i in range(len(b)):
                    if b[i].word == string:
                        print(b[i].people)
            if number == "6":
                stringlist = []
                friendlist = []
                string = input("단어를 입력하세요")
                for i in range(len(b)):
                    if b[i].word == string:
                        stringlist = b[i].people

                for j in range(len(stringlist)):
                 for i in range(len(a)):
                    p = a[i].first
                    judge = 0
                    while p is not None:
                        if a[p.n].name == stringlist[j]:
                            judge = 1
                        p = p.next
                    if judge == 1:
                        friendlist.append(a[i].name)

                print(friendlist)
            if number == "7":
                if len(deletedword) >= 1:
                  print(deletedword)
                  print("는 이미 제거되었습니다.")
                string = input("단어를 입력하세요")
                deletedword.append(string)
                wordlist1 = []
                q = -1
                for i in range(len(b)):
                    if b[i].word == string:
                        wordlist1 = b[i].people
                        q = i
                if q >0:
                 b.remove(b[q])

                for i in range(len(a)):
                  for j in range(len(wordlist1)):
                    if a[i].name == wordlist1[j]:
                        a[i].delword(string)
            if number == "8":
                h1 = -1
                h2 =  0
                h3 =  0
                h4 =  0
                deletelist = []
                stringuselist = []
                if len(deleteduser) >= 1:
                    print(deleteduser)
                    print("는 이미 제거되었습니다.")
                string = input("단어를 입력하세요")
                for i in range(len(b)):
                    if b[i].word == string:
                        stringuselist = b[i].people
                        h1 = i
                deleteduser = deleteduser + stringuselist

                if h1 > 0:
                        b.remove(b[h1])

                while h2 != len(stringuselist):
                    for i in range(len(a)):
                        if a[i].name == stringuselist[h2]:
                            deletelist = a[i].word
                    for i in range(len(deletelist)):
                        for j in range(len(b)):
                         if b[j].word == deletelist[i]:
                             b[j].delete(stringuselist[h2])
                    h2 +=1

                while h3 != len(stringuselist):
                    for i in range(len(a)):
                        if a[i].name == stringuselist[h3]:
                            h2 = i
                    a.remove(a[h2])
                    h3 +=1
                while h4 != len(stringuselist):
                    for i in range(len(a)):
                        prev = a[i].first
                        p = a[i].first.next
                        if a[prev.n] == stringuselist[h4]:
                            a[i].first = p
                        while p is not None:
                            if a[p.n].name == stringuselist[h4]:
                                prev.next = p.next
                            prev = p
                            p = p.next
                    h4 +=1

            if number == "9":
                print("감사합니다.")

menu()
