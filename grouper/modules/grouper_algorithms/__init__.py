import pandas as pd
import argparse
def kmeans(matrix, n_clusters):
    '''
    kmeans algorithm
    '''

    parse = argparse.ArgumentParser(description='Kmeans algorithm', usage='-n 2')

    parse.add_argument('-n', '--n_clusters', help = 'Set the number of clusters that Kmeans will use to group samples.',type = int, action = 'store', default = 2)

    from sklearn.cluster import KMeans

    print('\nTransposed Matrix:')
    print(matrix)

    model = KMeans(n_clusters = n_clusters)

    return model.fit_predict(matrix)