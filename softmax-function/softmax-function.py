import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x = np.asarray(x,dtype=float)

    
    # if x.ndim == 1 :
    #     max_x = np.max(x)
    #     numerator = np.exp(x - max_x)
    #     denominator_exponent = np.exp(x- max_x)
    #     prob = numerator / np.sum(denominator_exponent)
    # else:
    #     max_x = np.max(x,axis=1,keepdims=True)
    #     numerator = np.exp(x - max_x)
    #     denominator_exponent = np.exp(x- max_x)
      
    #     prob = numerator / np.sum(denominator_exponent,axis=1).reshape(max_x.shape)
    #     print('prob',prob)
    # return prob
    #efficient solution
    if x.ndim == 1:
        max_x = np.max(x)
        exp_shifted = np.exp(x-max_x)
        return exp_shifted / np.sum(exp_shifted)
    else:
        max_x = np.max(x,axis = 1,keepdims = True)
        exp_shifted = np.exp(x - max_x)
        return exp_shifted / np.sum(exp_shifted,axis=1, keepdims=True)

 