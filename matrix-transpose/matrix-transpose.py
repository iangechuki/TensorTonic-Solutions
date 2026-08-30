import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    #return np.transpose(A)
    A_T = []
    curr_shape = shape(A)
    n_cols = curr_shape[1]
    n_rows = curr_shape[0]
    A_flattened = flat(A)
    print("flattened A",A_flattened)
    for i in range(n_cols):
        row = []
        for j in range(n_rows):
            row.append(A_flattened[j*n_cols+ i])
        A_T.append(row)
    print("final",A_T)
    return np.array(A_T)
def shape(ndarray:list):
    if isinstance(ndarray,list):
        outermost_shape = len(ndarray)
        row_size = shape(ndarray[0])
        return (outermost_shape,*row_size)
    else:
        return ()
def flat(ndarray):
    output = []
    for item in ndarray:
        if isinstance(item,list):
            output.extend(flat(item))
        else:
            output.append(item)
    return output