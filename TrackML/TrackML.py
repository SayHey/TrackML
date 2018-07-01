import os
 
from trackml.dataset import load_event
from feature_extraction import *
from clusterer import *

# Load Data
data_path = '../Data/train_100_events/'
event_prefix = 'event000001000'
hits, cells, particles, truth = load_event(os.path.join(data_path, event_prefix))


# Extract features
features = helix_transform(hits.x.values, hits.y.values, hits.z.values)

# Perform clustering
try_clustering(hits, truth, np.transpose(features))

