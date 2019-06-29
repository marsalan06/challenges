import Mod_3rd_chal
l_1=[]
l_2=[]
l_3=[]
mon_1=[]
mon_2=[]
mon_3=[]
while True:
    user_in=str(input("to enter press E and quite X :"))
    if user_in =="e" or user_in=="E":
        choice_in=str(input("enter choice others(OTR), salary(SLR) & entertainment (ENT): "))
        if choice_in=="otr" or choice_in=="OTR":
            while True:
                indl={str(input("enter month: ")):str(input("enter amount: "))}
                mon_1.append(indl)
                print("for other expenses:","-")
                print(mon_1)
                ques=str(input("press c to cont to get final list and its conformance or any other key to continue: "))
                if ques== "c" or ques=="C":
                    print(Mod_3rd_chal.list_add(mon_1,l_1))
                    print(Mod_3rd_chal.mode_list(l_1))
                    break
        elif choice_in=="SLR" or choice_in=="slr":
            while True:
                indl={str(input("enter month: ")):str(input("enter amount: "))}
                mon_2.append(indl)
                print("for salary expenses:","-")
                print(mon_2)
                ques=str(input("press c to cont to get final list and its conformance or any other key to continue: "))
                if ques== "c" or ques=="C":
                    print(Mod_3rd_chal.list_add(mon_1,l_1))
                    print(Mod_3rd_chal.mode_list(l_1))
                    break
        elif choice_in=="ent" or choice_in=="ENT":
            while True:
                indl={str(input("enter month: ")):str(input("enter amount: "))}
                mon_3.append(indl)
                print("for entertainment expenses:","-")
                ques=str(input("press c to cont to get final list and its conformance or any other key to continue: "))
                if ques== "c" or ques=="C":
                    print(Mod_3rd_chal.list_add(mon_1,l_1))
                    print(Mod_3rd_chal.mode_list(l_1))
                    break
        else:
            print("give a valid entry _!_")
    elif user_in == "x" or user_in=="X":
        print("for other expenses","-")
        print(mon_1)
        print("for salary expenses","-")
        print(mon_2)
        print("for entertainment expenses","-")
        print(mon_3)
        print("exiting program")
        break
        

