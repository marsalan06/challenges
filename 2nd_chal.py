"""pythagoren triples"""
while True:
    user_input=int(input("enter no: "))
    a=0
    b=0
    c=0
    d=1
    while (d<=user_input):
        """first loop entery"""
        for i in range (1,user_input):
            """secod loop entery"""
            b=2*(d*i)
            a=abs((d**2)-(i**2))
            c=(d**2)+(i**2)
            f=a+b+c
            if ((a+b+c)==user_input):
                print("breaking")
                break
        d+=1
        if ((a+b+c) == user_input):
            print("a: "+str(a)+" b: "+str(b)+" c: "+str(c))
            break
        print("not found ending loop")
        break
        


