def bisection_method(func, a:float, b:float, error:float):
    """
    Bisection method for finding roots of a function.
    Parameters:
    func: function for which the root is to be found
    a: lower bound of the interval
    b: upper bound of the interval
    error: acceptable error margin for the root estimate
    """
    
    try:
        assert func(b)*func(a) < 0
    except AssertionError:
        return "No roots eroot_estimateist in given bounds."
    
    iteration = 1
    root_estimate = (a+b)/2
    interval_length = (b - a)/2


    while func(root_estimate) != 0 and abs(interval_length) > error:

        if func(a)*func(root_estimate) < 0:
            b = root_estimate
        elif func(root_estimate)*func(b) < 0:
            a = root_estimate
        
        root_estimate = (a+b)/2
        iteration += 1
        interval_length /= 2
        # print(f"Iteration {i}: root_estimate = {root_estimate}, f(root_estimate) = {func(root_estimate)}")
    
    else:
        print(f"Number of iterations: {iteration}")
        return root_estimate

def main():
    print(bisection_method(lambda x: x**3 + x -4, 1, 4, 0.001))

if __name__ == "__main__":
    main()