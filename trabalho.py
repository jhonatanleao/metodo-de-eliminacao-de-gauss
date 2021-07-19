import numpy as np

def verificaMatrizA(linhaA, colunaA):
	if linhaA == colunaA:
		return 1
	else:
		return 0

def verificaMatrizB(linhaA, linhaB, colunaB):
	if colunaB != 1 or linhaA != linhaB:
		return 0
	return 1

def subSucessiva(linhaA, A, B, X):	
	for i in range((linhaA-1), -1, -1):
		X[i] = B[i]
		for j in range((linhaA-1), 0, -1):
			if i != j:
				X[i]= X[i] - A[i][j] * X[j]
		X[i] = X[i]/A[i][i]

def eliminacao_gaussA(linhaA, A, B):
	for i in range(1, linhaA):
		for j in range(i, linhaA):
			matAUX = 0
			matAUX = A[j][i-1] / A[i-1][i-1]						
			for k in range(j,j+1):
				A[k] = A[k] - matAUX * A[i-1]
				B[k] = B[k] - matAUX * B[i-1]


def read_file(path):
	shape = tuple(
		np.loadtxt(
			fname=path, 
			dtype=int, 
			delimiter=',', 
			max_rows=1, 
			usecols=(0, 1)
			)
	)
	if verificaMatrizA(shape[0], shape[1]):
		A = np.loadtxt(
			fname=path, 
			dtype=float, 
			delimiter=',', 
			skiprows=1, 
			max_rows=shape[0], 
			usecols=np.arange(0, shape[1])
			)
		B = np.loadtxt(
			fname=path, 
			dtype=float, 
			delimiter=',', 
			skiprows=(shape[0] + 1), 
			max_rows=shape[0], 
			usecols=np.arange(0, shape[1])
		)
		return A, B
	else:
		exit(1)

def main():
	A = np.array([[3, 2, 4], [1, 1, 2], [4, 3, -2]], dtype = np.float64)
	B = np.array([[1], [2], [3]], dtype = np.float64)
	X = np.array([[0], [0], [0]], dtype = np.float64)
	(linhaA, colunaA) = A.shape
	(linhaB, colunaB) = B.shape
	x = verificaMatrizA(linhaA, colunaA)
	y = verificaMatrizB(linhaA, linhaB, colunaB)

	if linhaA != colunaA or colunaB != 1 or linhaA != linhaB:
		return 0	

	eliminacao_gaussA(linhaA, A, B)
	subSucessiva(linhaA, A, B, X)
	print(A)	
	print('')
	print(B)
	print('')
	print(X)

if __name__ == '__main__':
	[A, B] = read_file('i01.csv')
	print(A)
	print(B)
