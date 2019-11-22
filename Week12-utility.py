        #   YOUR GITHUB REPO 
        #   Charles Collins 
        #  ​CSCI 102 – Section A 
        #   Week 11 - Part B 

def PrintOutput(words):
    print("OUTPUT",words)

def LoadFile(filename):
    z = open(filename,'r')
    with open(filename) as f:
        mylist = f.read().splitlines() 
    return mylist

def UpdateString(string, let, number):
    mylist = []
    for x in range(len(string)):
        mylist.append(string[x])
    mylist[number] = let
    makeitastring = ''.join(map(str, mylist))
    print('OUTPUT',makeitastring)
    
def FindWordCount(inputlist,inputstring):
    mystring = ''
    for i in inputlist:
        mystring += i
    return mystring.count(inputstring)
        
    
def ScoreFinder(players,scores,name):
    namelist = []
    for i in range(len(name)):
        namelist.append(name[i])
    namelist[0] = namelist[0].upper()
    namestring = ''.join(map(str, namelist))
    x = players.index(namestring)
    print(namestring,'got a score of',scores[x])
    
def Union(list1,list2):
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2

def Intersection(list1,list2):
    mylist = []
    for i in list1:
        if i in list2:
            mylist.append(i)
    return mylist

def NotIn(list1,list2):
    mylist = []
    for i in list1:
        if i not in list2:
            mylist.append(i)
    return mylist
