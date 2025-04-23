import matplotlib.pyplot as plt
import numpy as np
x = [0,1,2,3,4]
y = [0,2,4,6,8]
y1=[0,2.5,5,12,18]
# Add a title (specify font parameters with fontdict)
plt.title('Easy Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})

plt.plot(x,y ,label='OneXRed', color='red', linewidth=2, marker='.', linestyle='--', markersize=10, markeredgecolor='blue')
plt.plot(x,y1, label='TwoBlue', color='#0000ff', linewidth=2, markersize=5, markeredgecolor='blue')
plt.hlines(y=[2],xmin=0,xmax=4)
# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
# Add a legend
plt.legend()
plt.show()