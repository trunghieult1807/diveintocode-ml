import time
import numpy as np
import matplotlib.pyplot as plt

THICKNESS = 0.00008

#Using exponentiation arithmetic
start = time.time()
folded_thickness_1 = THICKNESS*2**43
elapsed_time = time.time() - start
#Convert to 10^4 kilometers
print("Thickness using exponentiation arithmetic: {:.2f}*10^4 kilometers".format(
    folded_thickness_1/(10000*1000)))
print("Time using exponentiation arithmetic : {}[s]".format(elapsed_time))

#Data list used to plot
data = []

#Using * operation and loop
def exp(n, e):
    if n == 0 and e == 0:
        return -1
    elif n == 0 and e != 0:
        return 0
    elif e == 0:
        return 1
    elif n == 1:
        return 1
    else:
        temp = 1
        for i in range(e):
            temp *= n
            data.append(temp)
        return temp


start = time.time()
folded_thickness_2 = THICKNESS*exp(2, 43)
elapsed_time = time.time() - start
print(
    "Thickness using loop: {:.2f}*10^4 kilometers".format(folded_thickness_2/(10000*1000)))
print("Time using loop : {}[s]".format(elapsed_time))
for i in range(len(data)):
    data[i] *= THICKNESS

#Graph 1
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(data, color='green', marker='o',
         linestyle='dotted', linewidth=3, markersize=0.5)
plt.tick_params(labelsize=20)
plt.show()

#Graph 2
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(data, color='yellow', marker='o',
         linestyle='dashed', linewidth=1)
plt.tick_params(labelsize=20)
plt.show()

#Graph 3
plt.title("thickness of folded paper")
plt.xlabel("number of folds")
plt.ylabel("thickness[m]")
plt.plot(data, color='blue')
plt.show()
print("The thickness is changing exponentially!")

