
import matplotlib.pyplot as plt
import numpy as np

y=np.array([35,25,25,15])
mylabes = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels=mylabes)
plt.legend(title='Four Fruites')
plt.show()