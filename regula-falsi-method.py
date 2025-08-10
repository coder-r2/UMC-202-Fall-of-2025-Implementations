def regula_falsi_method(a:float, b:float, func, error:float):
    """
    Regula Falsi method for finding roots of a function.

    Parameters:
    a: lower bound of the interval
    b: upper bound of the interval
    func: function for which the root is to be found
    error: acceptable error margin for the root estimate
    
    Returns:
    The estimated root of the function.
    """

    try:
        assert func(b)*func(a) < 0
    except AssertionError:
        return "No roots exist in given bounds."
    
    iteration = 1
    root_estimate = (a*func(b) - b*func(a)) / (func(b) - func(a))

    while abs(func(root_estimate)) > error:
        if func(root_estimate) * func(a) < 0:
            b = root_estimate
        else:
            a = root_estimate

        root_estimate = (a*func(b) - b*func(a)) / (func(b) - func(a))
        iteration += 1
    
    print(f"Number of iterations: {iteration}")
    return root_estimate

def main():
    print(regula_falsi_method(0, 1.3, lambda x: x**10 - 1, 0.001))

if __name__ == "__main__":
    main()
