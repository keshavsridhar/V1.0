from copy import deepcopy
file1 = open(r'\Input_File.txt','r').read().upper()
source = input("Enter source: ").upper()
target = input("Enter target: ").upper()

l1 = file1.split('\n')
l2 = []
val=True
dict1={}
dict_new={}

def populate_dict():
    global dict1
    global l2
    l2=[]
    dict1.clear()
    for x in l1:
        y = x.split(',')
        z = x.split(',')
        l2.append(z)
        y[0], y[1] = y[1], y[0]
        ','.join(y)
        l2.append(y)
    for a in l2:
        if a[0] in dict1:
            dict1[a[0]] = dict1[a[0]]+[a[1]]
        else:
            dict1[a[0]] = [a[1]]
    return

def DFS ( d , source , target , path = [] ):
    global val
    q = 0
    if source not in path:
        path=path+[source]
    if source==target and val==True:
        val=False
        print(path)
        return
    try:
        k=len(d[source])
    #print(path,source,dict1[source])
        while q <= k:
            try:
                if d[source] == []:
                    path = path[:-1]
                    source = path[-1]
                    DFS(d,source, target, path)
                else:
                    source1=d[source].pop()
                    if source1 in path:
                        continue
                    else:
                        DFS(d, source1, target, path)
                        break
            except IndexError:
                break
    except KeyError:
        path = path[:-1]
        source = path[-1]
        DFS(d,source, target, path)
    return

def IDS(source,target,d=0,path=[]):
    global dict1
    dict3=deepcopy(dict1)
    d=0
    path=[source]
    while d<=len(dict1)-1 :
        if target in path:
            break
        for k in path:
            for w in dict1[k]:
                if w not in path:
                    path=path+[w]
        dict_new={i:dict3[i] for i in path}
        DFS(dict_new,source,target)
        d+=1
        print(path)
    print("Depth: ",str(d))

populate_dict()
IDS(source,target)


