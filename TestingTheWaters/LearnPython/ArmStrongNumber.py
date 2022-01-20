
var=211
def FindArmStrongNumber(var):
    listofnumber=list(str(var))
    strvar=str(var)        
    lenofvar=len(str(var))    
    list2 = [int(number) ** lenofvar for number in listofnumber]
    sumofnum=sum(list2)
    # print(lenofvar)
    # print(var)
    # print(strvar)
    # print(list2)
    # print(sumofnum)
    if var==sumofnum:
        print("{} is Armstrong Number".format(var))
    else:
        print("{} is not a Armstrong Number".format(var))
    
FindArmStrongNumber(var)