def kmeans(matrix, args):
    '''
    kmeans algorithm
    '''
    from sklearn.cluster import KMeans

    # DELETE THIS
    print('\nTransposed Matrix:')
    print(matrix)

    model = KMeans(n_clusters = args['n_clusters'])

    return model.fit_predict(matrix)