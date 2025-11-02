import sys
sys.path.insert(0, 'src')
from supertropical import SupertropicalMatrix

A = SupertropicalMatrix([[2, 1], [1, 3]])
b = SupertropicalMatrix([[5], [4]])

print('Matrix A:')
for i in range(2):
    print(f'  [{A[i,0]} {A[i,1]}]')

print('\nVector b:')
for i in range(2):
    print(f'  [{b[i,0]}]')

perm = A.permanent()
print(f'\nPermanent: {perm} (tangible: {perm.is_tangible()})')

x = A.solve(b)
print('\nSolution x:')
for i in range(2):
    print(f'  [{x[i,0]}]')
