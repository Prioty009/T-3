import numpy as np
import matplotlib.pyplot as plt
k=150
s=np.linspace(100,200,500)
p=5
#(a)
long_call_payoff=np.maximum(s-k,0)
long_call_profit=long_call_payoff-p
#(b)
short_call_payoff=-long_call_payoff
short_call_profit=short_call_payoff+p

#(c)
long_put_payoff=np.maximum(k-s,0)
long_put_profit=long_put_payoff-p
#(d)

short_put_payoff=-long_put_payoff
short_put_profit=short_put_payoff+p

#plot
fig=plt.figure()
plt.subplot(2,2,1)
plt.plot(s,long_call_payoff,linestyle='--')
plt.plot(s,long_call_profit)
plt.xlabel("Stock price")
plt.ylabel("payoff/profit")

plt.grid('True')


plt.subplot(2,2,2)
plt.plot(s,short_call_payoff,linestyle='--')
plt.plot(s,short_call_profit)
plt.xlabel("Stock price")
plt.ylabel("payoff/profit")

plt.grid('True')


plt.subplot(2,2,3)
plt.plot(s,long_put_payoff,linestyle='--')
plt.plot(s,long_put_profit)
plt.xlabel("Stock price")
plt.ylabel("payoff/profit")

plt.grid('True')


plt.subplot(2,2,4)
plt.plot(s,short_put_payoff,linestyle='--')
plt.plot(s,short_put_profit)
plt.xlabel("Stock price")
plt.ylabel("payoff/profit")
plt.grid('True')
plt.show()





