import argparse
import functools
from modules.grouper_algorithms import kmeans
from os.path import dirname, isdir, exists
from os import mkdir
import pandas as pd
import sys

FILE_PATH = dirname(__file__.replace('\\', '/'))

# Chosen algorithm by user to grouper samples
op_algorithm = sys.argv[1] if len(sys.argv) > 1 or sys.argv[1] == '' else 'kmeans'

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
parse.add_argument(
    '-on',
    '--output_name',
    help = 'Name for the taxam grouper file.',
    type = str,
    action = 'store',
    default = 'TaxAM_grouper'
)
# Trash flag
parse.add_argument(
    op_algorithm,
    help = 'Trash flag to store alrithm type',
    type = str,
    action = 'store',
    default = None
)

# Check if op_algorithm is a valid algorithm
if op_algorithm not in algorithms_list:
    exit(op_algorithm + ' is not a valid algorithm.\nAlgorithms list: '\
        + str(algorithms_list))
    
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

# Matriz as dataframe
matrix = pd.read_csv(
    args['file_path'],
    delimiter = '\t',
    index_col= 'TaxAM'
)

transposed_matrix = matrix.transpose()
groups = algorithms[op_algorithm]['function'](transposed_matrix, args)

OUTPUT_FOLDER_PATH = FILE_PATH + '/../output_groups/'
args['output_name'] += '.csv'
if not isdir(OUTPUT_FOLDER_PATH):
    mkdir(OUTPUT_FOLDER_PATH)
if not exists(OUTPUT_FOLDER_PATH + args['output_name']):
    with open(OUTPUT_FOLDER_PATH + args['output_name'], 'w') as file:
        file.write(groups)
    print(OUTPUT_FOLDER_PATH + args['output_name'] + ' was saved.')
else:
    exit(OUTPUT_FOLDER_PATH + args['output_name'] + ' already exists.')
