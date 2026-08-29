import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    # Write code here
    lambda_ = 1.0507009873554804934193349852946
    alpha_ = 1.6732632423543772848170429916717

    result = []
    for val in x:
        if val > 0:
            result.append(lambda_*val)
        else:
            result.append(lambda_*alpha_*(math.exp(val)-1))
    return result
    #consice
    #return [lambda_ * val if val > 0 else lambda_ * alpha_ * (math.exp(val) - 1)for val in x]