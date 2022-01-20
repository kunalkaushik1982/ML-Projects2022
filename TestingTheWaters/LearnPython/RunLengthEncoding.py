#AAAABBBBCCCCCCCC-->4A4B8C
#AABCCA--->2A1B2C1A
input='AABCCA'
def RunLenghtEncoding(input):
    listofinput=list(input)
    print(listofinput)
    setofinput=set(listofinput)
    print(setofinput)
    output=''
    for item in setofinput:
        cnt=listofinput.count(item)
        output=(str(cnt)+''+item)+output
        cnt=0
    
    print(output)
    #return output
    
RunLenghtEncoding(input)