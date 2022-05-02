def kmeans(matrix, args):
    '''
    kmeans algorithm
    '''
    from sklearn.cluster import KMeans

    model = KMeans(n_clusters = args['n_clusters'])

    prediction = model.fit_predict(matrix)

    prediction_groups = set(prediction)

    groups = {}

    for pred_index, group in enumerate(prediction):
        sample = matrix.index[pred_index]
        try:
            groups[group].append(sample)
        except:
            groups[group] = [sample]
    
    csv_str = ''
    for values in groups.values():
        csv_str += ','.join(values) + '\n'

    return csv_str