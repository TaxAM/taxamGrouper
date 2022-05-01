import argparse
import sys
import functools
from modules.grouper_algorithms import kmeans
import pandas as pd

# Chosen algorithm by user to grouper samples
op_algorithm = sys.argv[1] if len(sys.argv) > 1 else 'kmeans'

algorithms_list = ['kmeans']

parse = argparse.ArgumentParser(description='Executes taxam grouper.', usage='python ./grouper/ "kmeans" -n 2.\nAlgorithms list: ' + str(algorithms_list))

algorithms = {
    'kmeans': {
        'function': kmeans,
        'flags': [
            functools.partial(parse.add_argument, '-n', '--n_clusters', help = 'Set the number of clusters that Kmeans will use to group samples.',type = int, action = 'store', default = 2)
        ]
    }
}

# Check if op_algorithm is a valid algorithm
if op_algorithm not in algorithms_list:
    op_algorithm = 'kmeans'
    
# Storing flags for algorithm chosen in parse
for flag in algorithms[op_algorithm]['flags']:
    flag()

# Arguments to the algorithms functions
args = parse.parse_args().__dict__

matrix = pd.read_csv(
    'grouper/src/saida-reino-no-one.taxam',
    delimiter = '\t',
    index_col= 'TaxAM'
)

# DELETE THIS
print('Original Matrix:')
print(matrix)

transposed_matrix = matrix.transpose()
groups = algorithms[op_algorithm]['function'](transposed_matrix, args)

# DELETE THIS
print('\nNumber of groups: 2.')
print('Groups:')
print(groups)

# [] Store variable groups in a csv file