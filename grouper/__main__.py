import argparse
from modules.grouper_algorithms import kmeans
import pandas as pd

algorithms = {
    'kmeans': kmeans,
    'somenthing': 'somenthing',
    'somenthing1': 'somenthing',

}

parse = argparse.ArgumentParser(description='Executes taxam grouper.', usage='python ./grouper/ -a "kmeans"')

parse.add_argument('-a', '--algorithm', help = 'Choise which algorithm taxam grouper will use to grouper samples.',type = str, action = 'store', default = 'kmeans', choices = algorithms.keys())

args = parse.parse_args().__dict__
# Chosen algorithm by user to grouper samples
op_algorithm = args['algorithm']

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