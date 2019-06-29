"""the  whole function takes the initial list and gets len, the ist loop get me 
    each dictionary then second loop starts and uses .values method to append in new empty list and 
    print it """
import statistics
#set_1 =[{'month': 'jan', 'amount': 2000}, {'month': 'feb', 'amount': 2300},{'month':'march','amount':2000},{'month':'april','amount':2000}]
def list_add(mon,l):
    p=len(mon)
    for i in range(0,p):
        u=mon[i]
        #print(u)
        for j in u.values():
            l.append(j)
    print(l)
    return(l)
def mode_list(l):
    print("Mode of given data set: ",l) 
    x=statistics.mode(l)
    print("is "+str(x))
    p=len(l)
    for i in range(0,p):
        if l[i]!=x:
            print(l[i],"-","non conformance")
        else:
            print(l[i],"-","data conformance")
    

"""o=[]
    for i in range(0,len(l)):
        o.append(l[i])
    print(o)
    return(l)"""

"""print("Mode of given data set is: ",l) 
x=statistics.mode(l)
print(x)
for i in range(0,p):
    if set_1[i]["amount"]!=x:
        print(set_1[i]["amount"],"-","non conformance")
    else:
        print(set_1[i]["amount"],"-","data conformance")"""

if __name__=="__main__":
    l=[]
    set_1 =[{'jan':2000}, {'feb': 2300},{'march':2000},{'april':2000}]
    list_add(set_1,l)
    mode_list(l)

    x  = {8:6 , 90:78}
    #for i in x.values():
        #print(i)

    l1 =[]
    for i in x.values():
        l1.append(i)
    print(l1)