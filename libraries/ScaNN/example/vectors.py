v1 = np.array([
        np.array([
           np.random.normal(1, 0.01),
           np.random.normal(0, 0.01),
           np.random.normal(0, 0.01)
        ])
        for _ in range(1000000)
     ]).astype(np.float32)

v2 = np.array([
        np.array([
           np.random.normal(0, 0.01),
           np.random.normal(1, 0.01),
           np.random.normal(0, 0.01)
        ])
        for _ in range(1000000)
     ]).astype(np.float32)

v3 = np.array([
        np.array([
           np.random.normal(0, 0.01),
           np.random.normal(0, 0.01),
           np.random.normal(1, 0.01)
        ])
        for _ in range(1000000)
     ]).astype(np.float32)
