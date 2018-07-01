import os
 
from trackml.dataset import load_event
from data import *

# Load Data
data_path = '../Data/train_100_events/'
event_prefix = 'event000001000'
hits, cells, particles, truth = load_event(os.path.join(data_path, event_prefix))


sequence = sort_layers(hits)
print(sequence)