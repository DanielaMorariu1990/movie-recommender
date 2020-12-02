import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import NMF
import joblib
import random

movies = pd.read_csv('./data/movies.csv')
ratings = pd.read_csv('./data/ratings.csv')
ratings_pivot = ratings.pivot(
    index='userId', columns='movieId', values='rating')
ratings_pivot.replace(np.nan, 0, inplace=True)
# convert ratings to dense?

if __name__ == "__main__":
    model = NMF(
        n_components=20,
        init='random',
        random_state=10,
        max_iter=1000
    )
    model.fit(ratings_pivot)
    model.reconstruction_err_
    joblib.dump(model, "nmf.sav")

    P = model.transform(ratings_pivot)
    Q = model.components_.T

    ratings_pred = Q.dot(P.T)
    print(ratings_pred.round(2))