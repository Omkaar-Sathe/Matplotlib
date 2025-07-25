
import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels=["Apples","Banans","Cherries","Dates"]

plt.pie(y,labels=mylabels)
plt.legend()
plt.show()