t = int(input("Enter number of test cases : "))
print ("\n")


if(t>=1 and t<=100):
    while(t!=0):
        flag = 0
        n = int(input("Enter size of array : "))

        if(n>=2 and n<=100000):
            a = []
            print("Enter array elements : ")
            for i in range(0,n):
                m = int(input())
                if(m>=1 and m<=1000000000):
                    a.append(m)
                else:
                    print("Value of element does not satisfy constraints")
                    break

            for i in range(0,n-1):
                if(a[i]%2 == 0):
                    for j in range(i+1,n):
                        if(a[j]%2==1):
                            flag = flag + 1
                        else:
                            continue
                else:
                    continue
            print(flag)

                
            t = t - 1

        else:
            print("Number of elements in the array do not satisfy constraints")
            break
else:
    print("Number of test cases do not satisfy constraints")
