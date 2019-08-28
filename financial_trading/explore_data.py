# standard libraries
from typing import List, Callable

# non-standard libraries
from matplotlib import pyplot as plt

# project libraries
from bonds import simple_bond_valuation

def plot_function(function: Callable, list_range: List[float], step: float = 0.01 ) -> None:
    """This function plots the given function over a range specified in the list_range

    Parameters
    -----------
    function: callable
        The function that will be called over the range

    list_range: List[float, float]
        A list that specifies the minimum (first element) and the maximum (second element) of the function graph
    
    step: float
        Specifies the step size of the plot. Set to 0.01 by default.

    Returns
    ----------

    None
        Doesn't return anything

    """

    x_values = range(list_range[0], list_range[1], step)

    y_values = list(function(x) for x in x_values)

    return y_values

if __name__ == "__main__":
    func = simple_bond_valuation(coupon_rate = 0.04, maturity = 20)
    print(func(market_rate = 0.06)) 
    ## this doesn't work like this. I want it to work, but it doesnt....
    