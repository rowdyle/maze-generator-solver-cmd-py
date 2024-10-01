import random, os, time

#     crate maze
#----------------------


class v2:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class blok:
    def __init__(self, look, ps ,From = 0, Type = 'wall', fcost = 0):
        self.fcost = fcost
        self.look = look
        self.fcost = fcost
        self.ps = ps
        self.Type = Type
        self.From = From


def sh(arry):
    os.system('cls')
    for i in arry:
        for j in i:
            print(j.look, end='')
        print()


def randomDric(x,y, arry, way):
    c = 0
    c2 = -2
    stop = False
    while True:
        a = [2 for i in range(100)]
        a.append(3)
        num = random.randrange(2)
        tx,ty = x,y
        if num:
            tx += random.randrange(-1,2)
        else:
            ty += random.randrange(-1,2)
        if tx < len(arry) - 1 and tx >= 1:
            if ty < len(arry) - 1 and ty >= 1:
                if arry[ty][tx].look == '||' and godornot(tx,ty,arry) < a[random.randrange(len(a))]:
                    break      
        c += 1
        if c > 5:
           try:
               x = way[c2].x
               y = way[c2].y
               c2 -= 1
               c = 0
           except:
               stop = True
               break

    return tx,ty, stop

def godornot(x,y,arry):
    num = 0
    try:
       if arry[y +1][x].look == '  ':
           num += 1
       if arry[y -1][x].look == '  ':
           num += 1
       if arry[y ][x-1].look == '  ':
           num += 1
       if arry[y ][x+1].look == '  ':
           num += 1
    except:
        pass
    return num



#    solver
#----------------

def startEnd(arry):
    ar = list()
    for i in range(len(arry)):
        for j in range(len(arry[i])):
            if arry[i][j].look == '  ':
                ar.append(v2(j,i))
    
    temp = random.randrange(len(ar))
    arry[ar[temp].y][ar[temp].x].look = 's '
    arry[ar[temp].y][ar[temp].x].type = 's'
    s = ar[temp]
    ar.remove(ar[temp])
    temp = random.randrange(len(ar))
    arry[ar[temp].y][ar[temp].x].look = 'e '
    e = ar[temp]

    return arry, s, e




def solver(o, Map, arry, oarry,e):
    if Map[o.ps.y +1][o.ps.x].Type == 'rek':
        Map[o.ps.y +1][o.ps.x].Type = 'o'
        Map[o.ps.y +1][o.ps.x].From = o
        oarry.append(Map[o.ps.y +1][o.ps.x])
    if Map[o.ps.y -1][o.ps.x].Type == 'rek':
        Map[o.ps.y -1][o.ps.x].Type = 'o'
        Map[o.ps.y -1][o.ps.x].From = o
        oarry.append(Map[o.ps.y -1][o.ps.x])
    if Map[o.ps.y ][o.ps.x-1].Type == 'rek':
        Map[o.ps.y ][o.ps.x-1].Type = 'o'
        Map[o.ps.y ][o.ps.x-1].From = o
        oarry.append(Map[o.ps.y ][o.ps.x-1])
    if Map[o.ps.y ][o.ps.x+1].Type == 'rek':
        Map[o.ps.y ][o.ps.x+1].Type = 'o'
        Map[o.ps.y ][o.ps.x+1].From = o
        oarry.append(Map[o.ps.y ][o.ps.x+1])
    
    maxf = 99999
    temp = 0
    for i in oarry:
        vec = v2(abs(e.x - i.ps.x), abs(e.y - i.ps.y))
        i.fcost = (max(vec.x,vec.y) - min(vec.x,vec.y)) * 10 + min(vec.x,vec.y) * 15
        if i.fcost < maxf:
            temp = i
            maxf = i.fcost

    arry.append(temp)
    oarry.remove(temp)
    temp.Type = 'f'
    for i in Map:
        for j in i:
            if j.ps == temp.ps:
                j = temp

    stop = False
    if temp.look == 'e ':
        stop = True

    return temp,Map,arry,oarry,stop


def theWay(o,Map,arry):
    while o.look != 's ':
        x,y = o.ps.x,o.ps.y
        Map[y][x].look = '* '
        o = o.From

    #for i in arry:
    #    if i.look == '  ':
    #        x,y = i.ps.x,i.ps.y
    #        Map[y][x].look = "' "

    return Map

#----------

while True:
    #maze
    #-------------
    try:
        size = 30
        Map = [[blok('||' , v2(i,j)) for i in range(size)]for j in range(size)]
        way = []
        x = random.randrange(size)
        y = 1
        while True:
            way.append(v2(x,y))
            Map[y][x].look = '  '
            Map[y][x].Type = 'rek'
            #sh(Map)
            #time.sleep(0.2)
            x,y,stop = randomDric(x,y,Map, way)
            if stop:
                break


        sh(Map)

        #solver
        #----------

        s = e = v2(0,0)
        Map,s,e  = startEnd(Map)
        sh(Map)
        print(s.x,s.y,'\n',e.x,e.y)
        Farry = list()
        Oarry = list()
        stop = False
        Next,Map,Farry,Oarry,stop = solver(Map[s.y][s.x],Map,Farry,Oarry,e)
        while stop == False:
            Next,Map,Farry,Oarry,stop = solver(Next,Map,Farry,Oarry,e)

        Map = theWay(Next.From,Map,Farry)

        sh(Map)

        os.system("pause")
    except:
        pass





