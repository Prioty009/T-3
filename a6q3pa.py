payments=[460,235,640,370,330,250]
annual_ir=0.045
quarter_per_year=4
quarter_ir=annual_ir/quarter_per_year
def present_value(payment,year):
    n=quarter_per_year*year
    return payment/((1+quarter_ir)**n)
present_values=[present_value(p,t+1) for t,p in enumerate(payments)]
total_PV=sum(present_values)
for t,pv in enumerate(present_values,start=1):
    print(f"{t} present value:{pv:.2f}")
print(f"total present value:{total_PV:.2f}")