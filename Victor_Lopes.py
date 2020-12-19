import numpy as np
from numba import jit

# 1
inicio = 1
fim = int(5e6)


@jit(nopython=True, fastmath={'reassoc', 'nsz'}, parallel=True)
def f(start: int, end: int):
	x = np.arange(start, end + 1)
	x = len(x[(x % 2 == 0.) & (x % 49 == 0.) & (x % 37 == 0.)])
	
	return x


print('Existem ' + str(f(inicio, fim)) + ' números que satisfazem as três condições.')


# 2
def g(tamanho: int, precisao=2):
	
	x = []
	for i in range(tamanho):
		if i % 2 == 0:
			x.append(3**i + 7*np.math.factorial(i))
		else:
			x.append(2**i + 4*np.log(i))
	
	x = np.asarray(x)
	return x, np.argmax(x), np.around(np.mean(x), precisao)


a, b, c = g(10)
print('O maior elemento do vetor, cujo valor é ' + str(a[b]) + ', se encontra na posição ' + str(b) + '.')
print('O valor médio do vetor é: ' + str(c) + '.')

# 3
alunos = {}
for n in range(5):
	nome = input('Nome do aluno ' + str(n + 1) + ': ')
	nota = input('Nota do aluno ' + str(n + 1) + ': ')
	alunos[nome] = float(nota)

maior_nota = max(alunos.values())
for m, n in alunos.items():
	if n == maior_nota:
		print('O aluno com a maior nota se chama ' + m + ' e sua nota é: ' + str(n) + '.')



