while True:

    n=int(input("Enter Number: "))


    for i in range(2,n):
        if n%i==0:
            num="not prime"
            break
        else:
            num="prime" 
            
                    
            

    print(num)    