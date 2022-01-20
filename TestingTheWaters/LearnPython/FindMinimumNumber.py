

def FindMinimum(var1,var2,var3):
    var=0
    listofnumber=[]
    listofnumber.append(var1)
    listofnumber.append(var2)
    listofnumber.append(var3)
    var=min(listofnumber)
    print("Minimum of between {},{},{} is {}".format(var1,var2,var3,var))
    
var1=5
var2=8
var3=2
FindMinimum(var1,var2,var3)