import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

plt.plot(x, y)
plt.title("Test Graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()