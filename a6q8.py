import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as spi

s = 32
sigma = 0.30
r = 0.05
prices = np.linspace(20,45,200)

def black_scholes_call(k,t):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t)/(sigma*np.sqrt(t))
    d2 = d1- sigma*np.sqrt(t)
    call_price = s*spi.norm.cdf(d1) - k*np.exp(-r*t)*spi.norm.cdf(d2)
    return call_price

def black_scholes_put(k,t):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t)/(sigma*np.sqrt(t))
    d2 = d1- sigma*np.sqrt(t)
    put_price = k*np.exp(-r*t)*spi.norm.cdf(-d2)-s*spi.norm.cdf(-d1) 
    return put_price


#(a)
k1 = 25
k2 = 30
t = 6/12
call_price_k1 = black_scholes_call(k1,t)
call_price_k2 = black_scholes_call(k2,t)

profit = np.maximum(prices -k1,0) -call_price_k1 - np.maximum(prices-k2,0) + call_price_k2

print('Final Stock price     Bull call spread')
for i in range(0,len(prices),20):
    print(f'  {prices[i]:.3f}                 {profit[i]:.3f}')

plt.plot(prices,profit,label='bull')

#(b)
k1 = 25
k2 = 30
t = 6/12
put_price_k1 = black_scholes_put(k1,t)
put_price_k2 = black_scholes_put(k2,t)

profit = np.maximum(k2-prices,0) -put_price_k2 - np.maximum(k1-prices,0) + put_price_k1

print('Final Stock price     Bear call spread')
for i in range(0,len(prices),20):
    print(f'  {prices[i]:.3f}                 {profit[i]:.3f}')

plt.plot(prices,profit,label='bear')

#(c)
k1 = 25
k2 = 30
k3 = 35
t = 1
call_price_k1 = black_scholes_call(k1,t)
call_price_k2 = black_scholes_call(k2,t)
call_price_k3 = black_scholes_call(k3,t)

profit = np.maximum(prices -k1,0) -call_price_k1 - 2*np.maximum(prices-k2,0) + 2*call_price_k2 + np.maximum(prices-k3,0) - call_price_k3

print('Final Stock price     Buterfly call spread')
for i in range(0,len(prices),20):
    print(f'  {prices[i]:.3f}                 {profit[i]:.3f}')

plt.plot(prices,profit,label='butterfy call')

#(d)
k1 = 25
k2 = 30
k3 = 35
t = 1
put_price_k1 = black_scholes_put(k1,t)
put_price_k2 = black_scholes_put(k2,t)
put_price_k3 = black_scholes_put(k3,t)

profit = np.maximum(k1-prices,0) -put_price_k1 - 2*np.maximum(k2-prices,0) + 2*put_price_k2 + np.maximum(k3 - prices,0) - put_price_k3

print('Final Stock price     Butterfly put spread')
for i in range(0,len(prices),20):
    print(f'  {prices[i]:.3f}                 {profit[i]:.3f}')

plt.plot(prices,profit,label='butterfy put')

#(e)
k2 = 30
t = 6/12
call_price_k1 = black_scholes_put(k2,t)
put_price_k1 = black_scholes_put(k2,t)

profit =np.maximum(prices - k2,0) - call_price_k1 + np.maximum(k2-prices,0) - put_price_k1

print('Final Stock price     straddle')
for i in range(0,len(prices),20):
    print(f'  {prices[i]:.3f}                 {profit[i]:.3f}')

plt.plot(prices,profit,label='straddle')

#(f)
K1 = 25
K2 = 35
T = 6/12
put_price_k1 = black_scholes_put(K1,T)
call_price_k2 = black_scholes_call(K2,T)

strangle = np.maximum(prices - K2,0) - call_price_k2 + np.maximum(K1- prices,0) - put_price_k1
print('\n(f)A strangle using options')
print('Final Stock Price     strangle')
for i in range(0,len(prices),20):
    print(f'    {prices[i]:<15.4f}   {strangle[i]:<15.4f}')

plt.plot(prices,strangle,label = 'strangle')

plt.axhline(0, color='black')
plt.title('Profit vs. Final Stock Price')
plt.xlabel('Final Stock Price')
plt.ylabel('Profit')
plt.legend()
plt.tight_layout()
plt.grid(True)
plt.show()
