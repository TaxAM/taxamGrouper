"""Collection of algorithms used to group samples

Functions
---------
kmeans(matrix, args)
    Uses kmeans algorithm to group the samples.
"""
def kmeans(matrix, args):
    """Uses kmeans algorithm to group the samples.

    Parameters
    ----------
    matrix : pandas.core.frame.DataFrame
        Each header value is an animal indexed by sample name.
    args : Especific args used to run this algorithm. Values used here:
        ['n_clusters'] : int
            The number of clusters to form as well as the number of centroids to generate.
        ['n_init'] : int
            Number of time the k-means algorithm will be run with different centroid seeds. The final results will be the best output of n_init consecutive runs in terms of inertia.
        ['max_iter'] : int
            Maximum number of iterations of the k-means algorithm for a single run.

    Returns
    -------
    str
        CSV with all samples grouped, each line is a group with different samples.
    """    
    from sklearn.cluster import KMeans

    model = KMeans(
        n_clusters = args['n_clusters'],
        n_init = args['n_init'],
        max_iter = args['max_iter']
    )

    prediction = model.fit_predict(matrix)

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