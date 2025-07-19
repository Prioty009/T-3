import numpy as np

t = 5
years = np.array([1,2,3,4,5])
Face_value = 100 
yeild_initial = 0.11
cupon_rate = 0.08 
yeild_new = 0.108
cupon_payment = cupon_rate*Face_value

#(a)
pv_cupon = cupon_payment*np.exp(-yeild_initial*years)
pv_face = Face_value*np.exp(-yeild_initial*t)
bond_price = np.sum(pv_cupon) + pv_face
print(f'Bond price = {bond_price:.2f}')

#(b)
weighted_time = years*pv_cupon
weighted_face = t*pv_face
duration = (np.sum(weighted_time) + weighted_face)/bond_price
print(f'Duration = {duration:.2f}')

#(c)
delta_yeild = -0.002
price_change = -delta_yeild*duration*bond_price
print(f' the effect on the bond’s price of a 0.2% decrease in its yield : {price_change:.2f}')

#(d)
pv_cupon_new = cupon_payment*np.exp(-yeild_new*years)
face_new = Face_value*np.exp(-yeild_new*t)
new_bond_price = np.sum(pv_cupon_new) + face_new
print(f'Price = {new_bond_price:.2f}')

price_diff = new_bond_price - bond_price
if np.abs(price_diff - price_change)<0.01:
    print('Verified')
else:
    print('Not verified')