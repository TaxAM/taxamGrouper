from modules.grouper_algorithms import kmeans
import pandas as pd

algorithms = {
    'kmeans': kmeans
}

matrix = pd.read_csv(
    './src/saida-reino-no-one.taxam',
    delimiter = '\t',
    index_col= 'TaxAM'
)


print('Original Matrix:')
print(matrix)

transposed_matrix = matrix.transpose()
groups = algorithms['kmeans'](matrix, 2)

print('\nNumber of groups: 2.')
print('Groups:')
print(groups)