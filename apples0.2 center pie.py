
import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])

mylabels=["Apples","Bananas","Cherries","Dates"]
myeplode =[0.2,0,0,0]

plt.pie(y, labels=mylabels,explode=myeplode)
plt.show()