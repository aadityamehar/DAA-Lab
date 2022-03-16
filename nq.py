x = [0] * 4

def qPlace(k, i):
	for j in range(k+1):
		if x[j] == i or (x[j] - i) == (j - k):
			return False
		return True


def nQueen(k, n):
	
	for i in range(n):
		if qPlace(k-1, i):
			x[k-1] = i+1
		if k == n:
			print(x)
		else:
			nQueen(k, n)


nQueen(1, 4)
