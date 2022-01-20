
ticketrate=37550.0;adultcount=2;childcount=2;discount=10;tax=7
def TicketCost(ticketrate,adultcount,childcount,discount,tax):
    costforadult=ticketrate*adultcount
    costforchild=(ticketrate*childcount)/3
    totalcostwithouttax=costforadult+costforchild
    totaltax=(totalcostwithouttax)*(tax/100)
    finalcost=(totalcostwithouttax+totaltax)
    discount=(finalcost)/discount
    finalcost=finalcost-discount
    print("Total cost for {} Adults and {} child is {} ".format(adultcount,childcount,finalcost))
    
    
TicketCost(ticketrate,adultcount,childcount,discount,tax)
    