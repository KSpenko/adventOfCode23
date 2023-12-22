import numpy as np 

# path = "test_day6.txt"
path = "input_day6.txt"

'''
This is a physics problem:
- T total time
- t time of pressing the button
- d distance
- v speed
- t' time of the competitor pressing the button
- d' distance of the competitor
- a acceleration = 1

v = a*t
d = v*(T-t) = a*t*(T-t) = t*(T-t) = t*T - t**2

optimal time, is where derivative dd/dt = 0
dd/dt = T - 2*t = 0
t = T/2

t' = (T - sqrt( T**2 - 4*d' ))/2
delta_t = T/2 - t'

if T is even, then delta_t -= 1
'''

with open(path) as f:
    content = f.readlines()
    times = np.array(content[0].split(":")[1].split(), dtype=int)
    distances = np.array(content[1].split(":")[1].split(), dtype=int)
    n = len(times)

    prod = 1
    for i in range(n):
        best_time = times[i]/2.
        
        disc = np.sqrt(times[i]**2 - 4*distances[i])
        tcompetitor = 0.5*( times[i] - disc )
        s = -tcompetitor**2. + tcompetitor*times[i] 

        print(tcompetitor, best_time, s)
        deltat = int( np.floor(best_time) - np.floor(tcompetitor) )*2

        if best_time%1 == 0:
            deltat -= 1
        print(deltat)
        prod *= deltat
    print(prod)