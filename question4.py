import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
cur_x = 10.0
cur_y = 8.0
precision = 0.000001  # Increased precision for better accuracy
max_iters = 10000     # Maximum number of iterations

# Define the function f(x, y)
def func(x, y):
    r = np.sqrt(x**2 + y**2)  # Calculate r
    return -0.4 + (x + 15) / 30 + (y + 15) / 40 + 0.5 * np.sin(r)

# Calculate the gradient of f(x, y) with respect to x and y
def grad(x, y):
    r = np.sqrt(x**2 + y**2)
    # Handle r = 0 to avoid division by zero
    if r == 0:
        return 0, 0
    grad_x = (1 / 30) + (x / r) * 0.5 * np.cos(r)
    grad_y = (1 / 40) + (y / r) * 0.5 * np.cos(r)
    return grad_x, grad_y

# Lists to store the path
x_values = [cur_x]
y_values = [cur_y]
z_values = [func(cur_x, cur_y)]

# Iteration counter
iters = 0

# Gradient Descent loop
while iters < max_iters:
    prev_x = cur_x
    prev_y = cur_y

    # Compute the gradients
    gradient_x, gradient_y = grad(prev_x, prev_y)

    # Update x and y using the gradients
    cur_x = cur_x - 0.1 * gradient_x
    cur_y = cur_y - 0.1 * gradient_y

    # Calculate the function value at the new point
    z = func(cur_x, cur_y)

    # Calculate the distance between points to check for convergence
    distance_path = np.sqrt((cur_x - prev_x)**2 + (cur_y - prev_y)**2)

    # Store values for visualization
    x_values.append(cur_x)
    y_values.append(cur_y)
    z_values.append(z)

    # Print current iteration and values
    print(f"Iteration {iters+1}: (x, y, z) = ({cur_x:.4f}, {cur_y:.4f}, {z:.4f}), Gradient = ({gradient_x:.4f}, {gradient_y:.4f})")

    # Check for convergence
    if distance_path < precision:
        break

    iters += 1

# Final result
print(f"\nThe local minimum occurs at (x, y) = ({cur_x:.4f}, {cur_y:.4f})")
print(f"The value of the function at this point is z = {z:.4f}")

# 3D Plot of the path taken by gradient descent
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values, marker='o', linestyle='-', color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('Gradient Descent Path for f(x, y)')
plt.show()
