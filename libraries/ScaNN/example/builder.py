builder = scann.scann_ops_pybind.builder(
    data,
    num_neighbors    =  10,
    distance_measure = 'squared_l2'  # or, alternatively: 'dot_product'
)
