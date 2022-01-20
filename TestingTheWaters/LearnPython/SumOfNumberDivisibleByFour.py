
def SumOfNumber():
    sum=0    
    while(True):
        var=int(input("Please share the number: ")) 
        #print(var)
        if(var%4==0):
            sum=sum+var
            print(sum)
        else:
            print("Not Divisible by 4")    
    
SumOfNumber()