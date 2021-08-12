import numpy as np
import sys 

def read_file(path):
    shape = tuple(
            np.loadtxt(
                fname=path,
                dtype=np.int64,
                delimiter=',',
                max_rows=1, 
                usecols=(0, 1)
            )
        )
    N, P = shape[0], shape[1]
    if N > 0 and P > 0:
        input = np.matrix(
                    np.loadtxt(
                        fname=path,
                        dtype=str,
                        delimiter=',',
                        max_rows=N, 
                        skiprows=1,
                        usecols=(0, 1)
                    )
                )
        X, Y = input[:, 0], input[:, 1]
        return N, P, X.astype(np.float64), Y.astype(np.float64)
    else:
        sys.exit("Tamanho de entrada inválido!")
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_file(sys.argv[1])
        N, P, X, Y = read_file(sys.argv[1])
        #print(f'vetor X:\n {X}')
        #print(f'vetor Y:\n {Y}')
        
        matrix_values = Y
        matrix_values = np.insert(arr=matrix_values, obj=1, values=X.T, axis=1)
        for i in np.arange(2, ((2 * P) + P + 1)):
            if i <= (2 * P):
                matrix_values = np.insert(
                    arr=matrix_values, 
                    obj=i, 
                    values=np.power(X, i).T, 
                    axis=1)
            else:
                matrix_values = np.insert(
                    arr=matrix_values, 
                    obj=i, 
                    values=np.multiply(matrix_values[:, i-(2*P)], matrix_values[:, 0]).T, 
                    axis=1)
        
        matrix_sums = np.zeros(shape=(2 * P) + P + 1)
        for i in np.arange(0, ((2 * P) + P + 1)):
            matrix_sums[i] = np.sum(a=matrix_values[:, i], dtype=np.float64)
        print(matrix_values)
        print(matrix_sums)

       