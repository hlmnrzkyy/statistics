import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat

data = pd.io.parsers.read_csv("data.csv")
dataArray = np.asarray(data)
spread1 = dataArray[:, 0]
spread2 = dataArray[:, 1]

print("Mean: ", [np.mean(spread1), np.mean(spread2)])
print("Median: ", [np.median(spread1), np.median(spread2)])
print("Mode: ", [stat.mode(spread1), stat.mode(spread2)])
print("Maximum: ", [np.max(spread1), np.max(spread2)])
print("Minimum: ", [np.min(spread1), np.min(spread2)])


plt.figure(1)
plt.boxplot([spread1, spread2], labels = ["x1", "x2"])
plt.title('Boxplot')
plt.show()




