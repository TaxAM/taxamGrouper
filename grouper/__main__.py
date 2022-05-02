import argparse
import functools
from posixpath import split
from modules.grouper_algorithms import kmeans
from os.path import exists
import pandas as pd
import sys

# Chosen algorithm by user to grouper samples
op_algorithm = sys.argv[1] if len(sys.argv) > 1 else 'kmeans'

algorithms_list = ['kmeans']

parse = argparse.ArgumentParser(description='Executes taxam grouper.', usage='python ./grouper/ "kmeans" -n 2.\nAlgorithms list: ' + str(algorithms_list))

algorithms = {
    'kmeans': {
        'function': kmeans,
        'flags': [
            functools.partial(
                parse.add_argument,
                '-n',
                '--n_clusters',
                help = 'Set the number of clusters that Kmeans will use to group samples.',
                type = int,
                action = 'store',
                default = 2
            )
        ]
    }
}
# Default flags
parse.add_argument(
    '-fp',
    '--file_path',
    help = 'Matrix to group.',
    type = str,
    action = 'store',
    default = None
)

# Check if op_algorithm is a valid algorithm
if op_algorithm not in algorithms_list:
    op_algorithm = 'kmeans'
    
# Storing flags for algorithm chosen in parse
for flag in algorithms[op_algorithm]['flags']:
    flag()

# Arguments to the algorithms functions
args = parse.parse_args().__dict__

# Check if the file is valid
if args['file_path'] != None and\
     args['file_path'].split('.')[-1].lower() == 'taxam' :
    # Check if matrix exists
    if not exists(args['file_path']):
        exit(args['file_path'] + ' does not exists.')
else:
    exit('You should inform a matrix valid file.')


matrix = pd.read_csv(
    args['file_path'],
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