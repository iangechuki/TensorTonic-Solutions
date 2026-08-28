import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x,dtype=float)

    
    if x.ndim == 1 :
        max_x = np.max(x)
        numerator = np.exp(x - max_x)
        denominator_exponent = np.exp(x- max_x)
        prob = numerator / np.sum(denominator_exponent)
    else:
        print(x.shape)
        max_x = np.max(x,axis=1,keepdims=True)
        print(max_x.shape)
        numerator = np.exp(x - max_x)
        denominator_exponent = np.exp(x- max_x)
        print('num',numerator)
        print("denom_exp",denominator_exponent)
        print("sum",np.sum(denominator_exponent,axis=1))
        prob = numerator / np.sum(denominator_exponent,axis=1).reshape(max_x.shape)
        print('prob',prob)
    return prob

 