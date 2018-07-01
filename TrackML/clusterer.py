#DBSCAN Clusterer

import numpy as np
import pandas as pd
from trackml.score import score_event

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

def predict(X, eps=0.008):
    cl = DBSCAN(eps, min_samples=1, algorithm='kd_tree')
    labels = cl.fit_predict(StandardScaler().fit_transform(X))
    return labels

#score
def create_one_event_submission(event_id, hits, labels):
    sub_data = np.column_stack(([event_id]*len(hits), hits.hit_id.values, labels))
    submission = pd.DataFrame(data=sub_data, columns=["event_id", "hit_id", "track_id"]).astype(int)
    return submission

def try_clustering(hits, truth, features):
    labels = predict(features)
    submission = create_one_event_submission(0, hits, labels)
    score = score_event(truth, submission)
    print("Your score: ", score)