


def simple_bond_valuation(coupon_rate: float, market_rate: float, maturity: float) -> float:
    """This function calculates the market value of a bond using the simple bond valuation formula. The formula is taken from the Palm Island Traders blog:
        https://palmislandtraders.blogspot.com/2010/05/trading-treasury-rates-with-etfs.html

    Paramaters
    ----------
    coupon_rate: float
        the initial interest rate of the bond upon issuance
    
    market_rate: float
        the prevailing market rate as a decimal meaning 4% is expressed as 0.04

    maturity: float in years
        the number of years until the bond matures with fractions allowed

    """

    market_value = coupon_rate*100*( 1 - 1/(1 + market_rate)**maturity)/ market_rate + 100 *  1/( 1 + market_rate)**maturity

    return market_value