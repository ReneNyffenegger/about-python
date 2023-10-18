query = np.array([ 0.5, 0.5, 0.5 ]).astype(np.float32)
neighbors, distances = searcher.search(query, final_num_neighbors=10)
