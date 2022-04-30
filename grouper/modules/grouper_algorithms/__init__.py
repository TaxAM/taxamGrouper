import pandas as pd
def kmeans(matrix, n_clusters):
    '''
    kmeans algorithm
    '''
    from sklearn.cluster import KMeans

    print('\nTransposed Matrix:')
    print(matrix)

    model = KMeans(n_clusters = n_clusters)

    return model.fit_predict(matrix)