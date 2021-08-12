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
                        dtype=np.float64,
                        delimiter=',',
                        max_rows=N, 
                        skiprows=1,
                        usecols=(0, 1)
                    )
                )
        X, Y = input[:, 0], input[:, 1]
        return N, P, X, Y
    else:
        sys.exit("Tamanho de entrada inválido!")
    

if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_file(sys.argv[1])
        N, P,X, Y = read_file(sys.argv[1])
        #print(f'vetor X:\n {X}')
        #print(f'vetor Y:\n {Y}')
        matrix = Y
        matrix = np.insert(arr=matrix, obj=1, values=X.T, axis=1)
        for i in np.arange(2, ((2 * P) + P + 1)):
            if i <= (2 * P):
                matrix = np.insert(
                    arr=matrix, 
                    obj=i, 
                    values=np.power(X, i).T, 
                    axis=1)
            else:
                matrix = np.insert(
                    arr=matrix, 
                    obj=i, 
                    values=np.multiply(matrix[:, i-(2*P)], matrix[:, 0]).T, 
                    axis=1)
        
        print(matrix)
        

       