builder = scann.scann_ops_pybind.builder(
    data,                             # numpy array containing the data points to be indexed
    num_neighbors        =  10,              # the number of neighbors to search for
    distance_measure     = "squared_l2"      # the distance metric to use (e.g., 'dot_product' or 'squared_l2')
)
