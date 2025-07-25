
import matplotlib.pyplot as plt
import numpy as np

#plot 1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("sales")

#plot 2

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("income")

plt.suptitle("my shop")
plt.show()