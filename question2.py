import matplotlib.pyplot as plt

# Step 1: Define the function and its gradient
def func(x):
    return (3 * x + 5) ** 2
def grad(x):
    return 2 * (3 * x + 5) * 3  # Derivative of the function with respect to x
# Step 2: Initialize variables
cur_x = 3  # Starting point
rate = 0.01  # Learning rate
precision = 0.0000001  # Precision for stopping
max_iters = 10000  # Maximum number of iterations
iters = 0  # Iteration counter
# Lists to store values for plotting
x_values = []
y_values = []
# Step 3: Implement Gradient Descent
while iters < max_iters:
    prev_x = cur_x
    gradient = grad(prev_x)  # Store the gradient value for clarity
    cur_x = cur_x - rate * gradient  # Update x based on gradient
    x_values.append(cur_x)
    y_values.append(func(cur_x))
    
    # Output point (x, y), value of gradient
    print(f"Iteration {iters}: x = {cur_x:.6f}, y = {func(cur_x):.6f}, gradient = {gradient:.6f}")
    
    # Check for convergence
    if abs(prev_x - cur_x) < precision:
        break 
    iters += 1
# Step 4: Output the final result
final_y = func(cur_x)  # Final y value
print(f"Local minimum occurs at x = {cur_x}, y = {final_y}, after {iters} iterations")

# Step 5: Plot the points
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.title('Gradient Descent Steps')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid(True)
plt.show()

