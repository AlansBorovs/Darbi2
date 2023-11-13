from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()

# Izveidojam 3D ass
ax = fig.add_subplot(111, projection='3d')

# Uzzīmējam vektoru no A līdz B
ax.quiver(*A, *AB, color='b')

ax.set_xlim([0, 3])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 4])

# Save the figure as an image
plt.savefig("vector_plot.png")
