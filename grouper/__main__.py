import argparse
import functools
from modules.grouper_algorithms import kmeans
import pandas as pd

parse = argparse.ArgumentParser(description='Executes taxam grouper.', usage='python ./grouper/ -a "kmeans"')

algorithms = {
    'kmeans': {
        'name': kmeans,
        'flags': [
            functools.partial(parse.add_argument, '-n', '--n_clusters', help = 'Set the number of clusters that Kmeans will use to group samples.',type = int, action = 'store', default = 2)
        ]
    }
}

parse.add_argument('-a', '--algorithm', help = 'Choise which algorithm taxam grouper will use to grouper samples.',type = str, action = 'store', default = 'kmeans', choices = algorithms.keys())

# Chosen algorithm by user to grouper samples
op_algorithm = parse.parse_args().__dict__['algorithm']

# Storing flags for algorithm chosen in parse


args = parse.parse_args().__dict__

print(algorithms)
exit('Stoped')
matrix = pd.read_csv(
    'grouper/src/saida-reino-no-one.taxam',
    delimiter = '\t',
    index_col= 'TaxAM'
)

print('Original Matrix:')
print(matrix)

transposed_matrix = matrix.transpose()
groups = algorithms[op_algorithm](transposed_matrix, 2)

print('\nNumber of groups: 2.')
print('Groups:')
print(groups)