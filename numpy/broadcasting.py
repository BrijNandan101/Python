prices=[100,200,300]

discount=10

final_prices=[]

for price in prices:
    final_price=price - (price * discount / 100)
    final_prices.append(final_price)

print(final_prices)


#with using numpy

import numpy as np
prices=np.array([100,200,300])
discount1=10

final_pricess=prices - (prices * discount/100)
print (final_pricess)