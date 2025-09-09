import matplotlib.pyplot as plt

x=[1,2,3,4,5]
plt.plot(x,x)

y=[]
for i in x:
    y.append(i**2)
plt.plot(x,y)

y=[]
for i in x:
    y.append(3**i)
plt.plot(x,y)

plt.suptitle("Graph for the three functions")
plt.show()