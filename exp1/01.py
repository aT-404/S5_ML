import matplotlib.pyplot as plt

x = [3, 4, 1.5, 4.5, 2, 3]
y = [5, 2, 4, 4, 2, 5]
a = [0, 0, 6, 6]
b = [1, 6, 6, 1]

plt.plot(a, b, label='BG')
plt.fill(a, b, 'green', alpha=1)
plt.plot(x, y, label='STAR')      # Outline of the star
plt.fill(x, y, 'red', alpha=1)  # Fill with sky blue color, semi-transparent


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('STAR')
plt.show()

