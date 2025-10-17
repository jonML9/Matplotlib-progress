import matplotlib.pyplot as plt

values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [values ** 2 for values in values]
cubes = [values ** 3 for values in values]

plt.scatter(values, squares)
plt.show()