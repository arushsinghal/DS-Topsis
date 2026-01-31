import pandas as pd
import numpy as np

def topsis(input_file, weights, impacts, output_file):
    data = pd.read_csv(input_file)
    matrix = data.iloc[:, 1:].values.astype(float)

    weights = np.array(weights)
    weights = weights / weights.sum()

    # Normalize
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm

    # Weighted normalized matrix
    weighted = normalized * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    data["Topsis Score"] = score
    data["Rank"] = data["Topsis Score"].rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
