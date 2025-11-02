import sys
sys.path.insert(0, 'src')
from supertropical import SupertropicalElement, SupertropicalMatrix
import itertools
import numpy as np

A = SupertropicalMatrix([[2, 1], [1, 3]])
n = 2
perms = list(itertools.permutations(range(n)))
print(f'Permutations: {perms}')

total_sum = SupertropicalElement(-np.inf)
for perm in perms:
    term_prod = SupertropicalElement(0.0)
    for i in range(n):
        term_prod = term_prod * A[i, perm[i]]
    print(f'Perm {perm}: product = {term_prod}')
    total_sum = total_sum + term_prod
    print(f'  Running sum = {total_sum}')

print(f'\nFinal permanent: {total_sum}')
print(f'Is ghost? {total_sum.is_ghost}')
