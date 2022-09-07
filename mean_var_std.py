import numpy as np

def calculate(list):
    lst=list
    if len(lst)<9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst) # convert list to numpy array
    mat = arr.reshape(3,3) # reshape the array to 3X3 matrix
    arr_mean = [np.mean(mat,axis=0).tolist(), np.mean(mat,axis=1).tolist(), np.mean(mat)]
    arr_var = [np.var(mat,axis=0).tolist(), np.var(mat,axis=1).tolist(), np.var(mat)]
    arr_std = [np.std(mat,axis=0).tolist(), np.std(mat,axis=1).tolist(), np.std(mat)]
    arr_max = [np.max(mat,axis=0).tolist(), np.max(mat,axis=1).tolist(), np.max(mat)]
    arr_min = [np.min(mat,axis=0).tolist(), np.min(mat,axis=1).tolist(), np.min(mat)]
    arr_sum = [np.sum(mat,axis=0).tolist(), np.sum(mat,axis=1).tolist(), np.sum(mat)]
    calculations = {"mean":arr_mean, "variance":arr_var, "standard deviation":arr_std, "max":arr_max, "min":arr_min, "sum":arr_sum}
    return calculations