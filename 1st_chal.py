re=str(input("enter binary string: "))
#x= re.split()
ls2=[]
for x in re:
    ls=x
    ls2.append(ls)
print(ls2)
count=0
for x in ls2:
    #l=["0","1"]
    if x == "1" or x == "0":
        #print(x)
        count+=1
        if count == len(ls2):
            print(re +" "+ ":True")
    else:
        print("False")
        break

"""for indiviual element"""
"""for x in ls2:
    l=["0","1","2","3","4","5","6","7","8","9"]
    if x in l:
        if int(x)*1==1 or int(x)*1==0:
            print(str(x)+" :True")
    else:
        print(str(x)+" :False")"""


        
