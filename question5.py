import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
cur_x = 10.0
cur_y = 8.0
precision = 0.000001  # Increased precision for better convergence
max_iters = 10000     # Maximum number of iterations

# Define the function f(x, y)
def func(x, y):
    r = np.sqrt(x**2 + y**2)  # Calculate r
    return -0.4 + (x + 15) / 30 + (y + 15) / 40 + 0.5 * np.sin(r)

# Calculate the gradient of f(x, y) with respect to x and y
def grad(x, y):
    r = np.sqrt(x**2 + y**2)
    if r == 0:
        return 0, 0  # Avoid division by zero
    grad_x = (1 / 30) + (x / r) * 0.5 * np.cos(r)
    grad_y = (1 / 40) + (y / r) * 0.5 * np.cos(r)
    return grad_x, grad_y

# ADAM Optimizer parameters
alpha = 0.001  # Increased learning rate for faster convergence
beta1 = 0.9
beta2 = 0.999
eps = 1e-8

# Initialize ADAM variables
m_x, m_y = 0, 0  # First moment
v_x, v_y = 0, 0  # Second moment

# Lists to store path for visualization
x_values, y_values, z_values = [cur_x], [cur_y], [func(cur_x, cur_y)]

# ADAM optimizer algorithm
iters = 0
while iters < max_iters:
    prev_x, prev_y = cur_x, cur_y  # Store previous values

    # Compute gradients
    gradient_x, gradient_y = grad(prev_x, prev_y)

    # Update first moment
    m_x = beta1 * m_x + (1 - beta1) * gradient_x
    m_y = beta1 * m_y + (1 - beta1) * gradient_y

    # Update second moment
    v_x = beta2 * v_x + (1 - beta2) * (gradient_x ** 2)
    v_y = beta2 * v_y + (1 - beta2) * (gradient_y ** 2)

    # Bias correction
    mhat_x = m_x / (1 - beta1 ** (iters + 1))
    mhat_y = m_y / (1 - beta1 ** (iters + 1))
    vhat_x = v_x / (1 - beta2 ** (iters + 1))
    vhat_y = v_y / (1 - beta2 ** (iters + 1))

    # Update x and y values
    cur_x = cur_x - alpha * mhat_x / (np.sqrt(vhat_x) + eps)
    cur_y = cur_y - alpha * mhat_y / (np.sqrt(vhat_y) + eps)

    # Calculate function value at the new point
    z = func(cur_x, cur_y)

    # Calculate distance between consecutive points for convergence check
    distance_path = np.sqrt((cur_x - prev_x)**2 + (cur_y - prev_y)**2)

    # Store values for plotting
    x_values.append(cur_x)
    y_values.append(cur_y)
    z_values.append(z)

    # Print current state
    print(f"Iteration {iters + 1}: (x, y, z) = ({cur_x:.4f}, {cur_y:.4f}, {z:.4f}), Gradient = ({gradient_x:.4f}, {gradient_y:.4f})")

    # Check for convergence
    if distance_path < precision:
        break

    iters += 1

# Print the final result
print(f"\nThe local minimum occurs at (x, y) = ({cur_x:.4f}, {cur_y:.4f})")
print(f"The value of the function at this point is z = {z:.4f}")

# Plotting the path on a 3D graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_values, y_values, z_values, marker='o', linestyle='-', color='b')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y)')
ax.set_title('ADAM Optimization on f(x, y)')
plt.show()
