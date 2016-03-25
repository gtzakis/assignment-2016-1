import argparse

parser = argparse.ArgumentParser()
parser.add_argument("onomarxeiou", help="name of file",default='.txt')
parser.add_argument("megethos", help="arithmos",
                    type=int, default=3)
args = parser.parse_args()
megethos = args.megethos
onomarxeiou = args.onomarxeiou


e=[]
lex={}
with open(onomarxeiou) as arxeio:
    
    
    for grammi in arxeio:
        kom=grammi.split()
        e.append(kom)
    for kom in e:
        kleidi = kom[0]
        timi = kom[1]

        if kleidi in lex:
            lex[kleidi].append(timi)
        else:
            lex[kleidi] = [timi]
        if timi in lex:
            lex[timi].append(kleidi)
        else:
            lex[timi] = [kleidi]
    for k in lex:
        t = k
        for k in lex:
            u = k
            if t !=u:
                tomi = list(set(lex[t]) & set(lex[u]))
                if len(tomi) < 1:
                    if u in lex[t]:
                        lex[t].remove(u)
                        lex[u].remove(t)
                        
            
    lexiko2 = {}
    for i in lex:
        kleidi2 = i
        for j in lex[kleidi2]:
            values = j
            if len(lex[kleidi2]) != 0:
                if kleidi2 not in lexiko2:
                    lexiko2[kleidi2] = [values]
                else:
                    lexiko2[kleidi2].append(values)
                    

    newlist = []
    for i in lexiko2:
        lista= []
        key = i
        lista.append(key)
        for j in lexiko2[key]:
            value = j
            lista.append(value)
        lista.sort(key=None, reverse=False)
        newlist.append(lista)
    i=0

 
    while i<len(newlist):
        j=0
        while j<len(newlist):
            if j!=i:
                if newlist[i] == newlist[j]:
                    del newlist[j]
            j= j+1
        i= i + 1
    i=0
    while i<len(newlist):
        i=i+1

    i=0
    while i<len(newlist):
        pleiada = tuple(newlist[i])
        print(pleiada)
        i=i+1
        
    
            
           

            
                    

