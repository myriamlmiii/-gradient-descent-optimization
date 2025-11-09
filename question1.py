import matplotlib.pyplot as plt
# Step 1: Define the function and its gradient
def func(x):
    return (3 * x + 5) ** 2

def grad(x):
    return 2 * (3 * x + 5) * 3  # Derivative of the function with respect to x

# Step 2: Initialize variables
cur_x = 3  # Starting point
rate = 0.01  # Learning rate
max_iters = 10000 # Fixed number of iterations (instead of stopping based on precision)
iters = 0  # Iteration counter

# Lists to store values for plotting
x_values = []
y_values = []
# Step 3: Implement Gradient Descent without a precision-based stopping condition
while iters < max_iters:
    prev_x = cur_x  # Store the current x value
    gradient = grad(prev_x)  # Calculate gradient at the current point
    cur_x = cur_x - rate * gradient  # Update x based on gradient
    cur_y = func(cur_x)  # Calculate y value for current x

    x_values.append(cur_x)  # Store x value for plotting
    y_values.append(cur_y)  # Store y value for plotting
    
    # Output point (x, y), value of gradient
    print(f"Iteration {iters}: x = {cur_x}, y = {func(cur_x)}, gradient = {grad(prev_x)}")

    iters += 1  # Increment iteration count
# Step 4: Output the final result
final_y = func(cur_x)  # Final y value at the end of fixed iterations
print(f"Local minimum occurs at x = {cur_x}, y = {final_y}, after {iters} iterations")

# Step 5: Plot the points
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.title('Gradient Descent Steps with Fixed Iterations')
plt.xlabel('x values')
plt.ylabel('y values')
plt.grid(True)
plt.show()
