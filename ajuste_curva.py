import numpy as np
import sys 
import trabalho

def read_file(path):
    """
    Faz a leitura do arquivo passado por parâmetro

    :parameters: 
        path -- file path (str)
    
    :return: 
        N -- tamanho do array (int)
        X -- array X (array)
        Y -- array Y (array)
        P -- grau do polinômio (int)
    """
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






def create_matrix_summations(array_summs, N, P):
    matrix_summations = np.zeros(shape=(P+1, P+1), dtype=np.float64)
    matrix_summations[0][0] = N
    count = 1
    for i in np.arange(0, P+1):
        if i != 0:
            count = i
        for k in np.arange(0, P+1):
            if i != 0 or k != 0:
                matrix_summations[i][k] = array_summs[count]
                # print(f"i{i},k{k}")
                count += 1


    return matrix_summations






def create_matrix_values(P, X, Y):
    """
    Cria a matrix de valores que vão ser usados no cálculo de ajuste de curva
    
    :parameters:
        X -- array X (array)
        Y -- array Y (array)
        P -- grau do polinômio (int)
    
    :return:
        matrix_values -- matriz com os valores para o cálculo (matriz)
        obs: 
        a matriz é construida da seguinte forma:
            posição 0 = array Y
            posição 1 = array X
            posições [2 .. (2 * P)] = array (X^i)
            posições [(2 * P + 1) .. ((2 * P) + P + 1)] = array Y*(arrays X)

    """ 
    matrix_values = Y
    matrix_values = np.insert(arr=matrix_values, obj=1, values=X.T, axis=1)
    for i in np.arange(2, ((2 * P) + P + 1)):
        if i <= (2 * P):
            matrix_values = np.insert(
                arr=matrix_values, 
                obj=i, 
                values=np.power(X, i).T, 
                axis=1
                )
        else:
            matrix_values = np.insert(
                arr=matrix_values, 
                obj=i, 
                values=np.multiply(matrix_values[:, i-(2*P)], matrix_values[:, 0]).T, 
                axis=1
                )
    
    return matrix_values
    
def create_array_summations(matrix_values, P):
    """
    Cria o vetor com o somatórios dos valores que vão ser usados para cálculo
    
    :parameters:
        matrix_values -- matriz com os valores para o cálculo (matriz)
        P -- grau do polinômio (int)
    :return:
        array_sums -- array com o somatório de cada coluna da matrix_values (array)
    """
    array_sums = np.zeros(shape=(2 * P) + P + 1)
    for i in np.arange(0, ((2 * P) + P + 1)):
            array_sums[i] = np.sum(a=matrix_values[:, i], dtype=np.float64)

    return array_sums


if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_file(sys.argv[1])
        N, P, X, Y = read_file(sys.argv[1])
        matrix_values = create_matrix_values(P, X, Y)
        array_sums = create_array_summations(matrix_values, P)
        matrix_summations = create_matrix_summations(array_sums, N, P)
        # print(matrix_values)
        print(array_sums)
        print(matrix_summations)


       