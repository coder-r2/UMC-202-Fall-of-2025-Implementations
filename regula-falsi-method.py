def regula_falsi_method(a:float, b:float, func, error:float):
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

    return root_estimate
