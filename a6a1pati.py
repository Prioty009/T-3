import numpy as np
r=0.0433
in_a=[225,215,250,225,205]
in_b=[220,225,250,250,210]
def present_value(payments,rate):
    pv=0
    for i,payment in enumerate(payments):
        t=i+1
        pv+=payment*np.exp(-rate*t)
    return(pv)
pv_A=present_value(in_a,r)
pv_B=present_value(in_b,r)
print(f"Investment of A={pv_A:.2f}")
print(f"Investment of A={pv_B:.2f}")

if pv_A>pv_B:
    print("investment A is preferable")
else:
    print("investment B is preferable")