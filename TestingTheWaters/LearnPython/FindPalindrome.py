from audioop import reverse


var='civic'
def FindPalindromeNumber(var):
    listofnumber=list(str(var))
    print(listofnumber)
    revlistofnumber=listofnumber.copy()
    revlistofnumber.reverse()
    print(revlistofnumber)
    if listofnumber==revlistofnumber:
        print("Palindrome")
    else:
        print("Not Palindrome")
    

FindPalindromeNumber(var)