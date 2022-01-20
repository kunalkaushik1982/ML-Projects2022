
# route consist of distance,passenger
dis=87
passenger=10
info={'fuelprice':70,'mileage':10,'ticketprice':80}
route={'distance':80,'countofpassenger':100}
def CalculateRouteProfit(route,info):
    distanceinroute=route['distance']
    fuelprice=info['fuelprice']
    totalfuelpriceinroute=distanceinroute*fuelprice
    totalticketpriceinroute=route['countofpassenger']*info['ticketprice']
    if(totalfuelpriceinroute<totalticketpriceinroute):
        return totalticketpriceinroute-totalfuelpriceinroute
    else:
        return -1
        
profit=CalculateRouteProfit(route,info)
print("Profit in this route is {}".format(profit))