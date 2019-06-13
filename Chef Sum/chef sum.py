t = int(input("Enter number of test cases : "))
print ("\n")

if(t>=1 and t<=100):
    while(t!=0):
        n = int(input("Enter size of array : "))

        if(n>=2 and n<=10000):
            k = int(input("Enter value of K(sum) : "))
            if(k>=1 and k<=1000000000):
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
                    for j in range(i+1,n):
                        sum1 = a[i]+a[j]
                        if(sum1 == k):
                            flag = 1
                            break
                        else:
                            flag = 0
                    if(flag == 1):
                        break
                if(flag == 1):
                    print("Yes")
                else:
                    print("No")

                t = t - 1

            else:
                print ("Value of K does not satisfy constraints")
                break
        else:
            print("Number of elements in the array do not satisfy constraints")
            break
else:
    print("Number of test cases do not satisfy constraints")
