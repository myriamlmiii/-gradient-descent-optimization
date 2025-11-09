import matplotlib.pyplot as plt

# Initial parameters
cur_x = 3
precision = 0.000001  # Stopping criterion
max_iters = 10000     # Maximum number of iterations

# Define the function and its gradient
def func(x):
    return (3 * x + 5) ** 2

grad = lambda x: 18 * x + 30  # Derivative of our function

# List of learning rates to test
learning_rates = [0.001, 0.01, 0.05, 0.1, 0.2, 0.3]

# Store the number of steps needed to reach the solution for each learning rate
steps_to_solution = []

# Run gradient descent for each learning rate
for rate in learning_rates:
    cur_x = 3  # Reset the starting point
    iters = 0  # Reset iteration count
    distance_path = 1  # Set initial distance path to a value larger than precision

    # Gradient descent loop
    while distance_path > precision and iters < max_iters:
        prev_x = cur_x  # Store current x value before updating
        cur_x = cur_x - rate * grad(prev_x)  # Update x using the gradient descent formula
        distance_path = abs(cur_x - prev_x)  # Calculate the change in x values
        iters += 1  # Increment iteration count

    # Record the number of iterations taken to reach the solution
    steps_to_solution.append(iters)
    print(f"Learning rate: {rate}, Steps to solution: {iters}")

# Plotting the results
plt.figure(figsize=(8, 6))
plt.plot(learning_rates, steps_to_solution, marker='o', linestyle='-', color='b')
plt.xscale('log')  # Logarithmic scale for better visualization of rates
plt.xlabel('Learning Rate')
plt.ylabel('Steps to Solution')
plt.title('Steps to Solution vs Learning Rate')
plt.grid(True)
plt.tight_layout()
plt.show()
