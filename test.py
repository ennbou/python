G = [
    [12.897,12.823,12.883,12.853,12.887],
    [12.866,12.882,12.944,12.846,12.923],
    [12.83,12.845,12.92,12.824,12.847],
    [12.835,13,12.921,12.826,12.855],
    [12.823,12.882,12.874,12.872,12.844],
    [12.895,12.946,12.804,12.795,12.849],
    [12.944,12.864,13.021,12.832,12.891],
    [12.803,12.821,12.975,12.776,12.85],
    [12.817,12.85,12.804,12.827,12.892],
    [12.894,12.872,12.83,12.887,12.809],
    [12.84,12.946,12.824,12.83,12.943],
    [12.821,12.871,12.844,12.88,12.863],
    [12.836,12.885,12.924,12.835,12.883],
    [12.89,12.829,12.904,12.986,12.819],
    [12.814,12.86,12.827,12.848,12.93],
    [12.912,12.869,12.909,12.861,12.973],
    [12.937,12.956,12.909,12.862,12.839],
    [12.923,12.823,12.903,12.907,12.922],
]

xbar = []
r = []
xbbar = 0
rbar = 0
lsc = []
lic = []
lscr= []
licr= []

print("satrt")

for i in G:
    xbar.append(float(format(sum(i) / len(i),".3f")))
    r.append(float(format(max(i)-min(i),".3f")))

xbbar = float(format(sum(xbar)/len(xbar),".3f"))
rbar = float(format(sum(r)/len(r),".3f"))

for i in range(len(G)):
    lic.append(float(format(xbbar - 0.577*rbar,".3f")))
    lsc.append(float(format(xbbar + 0.577*rbar,".3f")))

    licr.append(float(format(0*rbar,".3f")))
    lscr.append(float(format(2.114*rbar,".3f")))


for i,j,x,y,z,w in zip(xbar,r,lic,lsc,licr,lscr):
    print(i,j,xbbar,x,y,z,w)


# libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# data
df=pd.DataFrame({'x': range(len(G)), 'y': xbar })
# plot
plt.plot( 'x', 'y', data=df, linestyle='-', marker='o')
plt.show()


