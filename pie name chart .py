
import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabels = ["Apllea","Banana","Cherries","Dates"]

plt.pie(y, labels=mylabels)
plt.show()