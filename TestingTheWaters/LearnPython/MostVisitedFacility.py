#[101,P,102,O,302,P,305,P] --> Pediatrics
#"O":"Orthopedics",
#"E":"ENT

facility={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
patient={101:'E',102:'O',302:'O',305:'P'}
def MostVisitedFacility(patient,facility):
    getkey=patient.keys()
    pcnt=ocnt=ecnt=0
    listofadmissioncnt=[]
    for keys in patient:
        faci=patient[keys]
        if(faci=='P'):
            pcnt=pcnt+1
        elif(faci=='O'):
            ocnt=ocnt+1
        else:
            ecnt=ecnt+1
    
    if (pcnt >= ocnt) and (pcnt >= ecnt):
        #largest = pcnt
        print(facility['P'])
    elif (ocnt >= pcnt) and (ocnt >= ecnt):
        #largest = ocnt
        print(facility['O'])
    else:
        #largest = ecnt
        print(facility['E'])
       
    #print(listofadmissioncnt)
    #print(getkey)
    
MostVisitedFacility(patient,facility)