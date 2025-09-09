import matplotlib.pyplot as plt

a=[1,1,4,4]
x=[3,4,4,3]
y=[2,3,3,2]
z=[1,2,2,1]

plt.plot(a, x, label='G')
plt.fill(a, x, 'orange', alpha=1)
plt.plot(a, y, label='BG')
plt.fill(a, y, 'white', alpha=1)
plt.plot(a, z, label='BG')
plt.fill(a, z, 'green', alpha=1)

plt.show()