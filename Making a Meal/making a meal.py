t = int(input("Enter number of test cases : "))
print ("\n")


if(t>=1 and t<=100):
    while(t!=0):
        m = int(input("Enter number of strings : "))
        s = []

        if(m>=1 and m<=100):
            c,o,d,e,f,h = 0,0,0,0,0,0

            print("\nEnter the contents")
            for i in range(0,m):
                a1 = input()
                a = a1.lower()
                s.append(a)


            for i in s:
                for j in range(0,len(i)):
                    if(i[j]=='c'):
                        c = c + 1
                    elif(i[j]=='o'):
                        o = o + 1
                    elif(i[j]=='d'):
                        d = d + 1
                    elif(i[j]=='e'):
                        e = e + 1
                    elif(i[j]=='h'):
                        h = h + 1
                    elif(i[j]=='f'):
                        f = f + 1
                    else:
                        continue

            codechef = 0
            while(c>-1 and o>-1 and d>-1 and e>-1 and h>-1 and f>-1):
                if(c>0 and o>0 and d>0 and e>0 and h>0 and f>0):
                    codechef = codechef + 1
                    c = c - 1
                    o = o - 1
                    e = e - 1
                    d = d - 1
                    h = h - 1
                    f = f - 1
                else:
                    break
    
            print("Number of meals = ",codechef)

            t = t - 1

        else:
            print("Number of elements in the array do not satisfy constraints")
            break

else:
    print("Number of test cases do not satisfy constraints")
