def newton_raphson_method(func, derivative, initial_guess, error, max_iterations=100):
    """
    Newton-Raphson method for finding roots of a function.
    
    Parameters:
    func: The function for which we want to find the root.
    derivative: The derivative of the function.
    initial_guess: Initial guess for the root.
    tolerance: The acceptable error margin.
    max_iterations: Maximum number of iterations to prevent infinite loops.
    
    Returns:
    The estimated root of the function.
    """
    x = initial_guess
    for i in range(max_iterations):
        fx = func(x)
        dfx = derivative(x)
        
        if dfx == 0:
            return "Derivative is zero. No solution found."
        
        x_new = x - fx / dfx
        
        if abs(x_new - x) < error:
            return x_new
        
        x = x_new
    
    raise ValueError("Maximum iterations reached. No solution found.")

def main():
    func = lambda x: x**2 - 2
    derivative = lambda x: 2*x
    initial_guess = 1.0
    error = 0.001
    
    root = newton_raphson_method(func, derivative, initial_guess, error)
    print(f"Estimated root: {root}")

if __name__ == "__main__":
    main()