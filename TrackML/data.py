import numpy as np

"""
8 - cilindrical module with 4 layers closest to tube, part of pixel detector
13, 17 - outer cylindrical moduls with 4 and 2 layers respectevly, parts of short strip and long strip
7 - disc module with 7 layers located in negative z-coordinate area, part of pixel detector
12, 16 - disc modules with 6 layers each located in negative z-coordinate area, part of short strip and long strip
9 - disc module with 7 layers located in positive z-coordinate area, part of pixel detector
14, 18 - disc modules with 6 layers each located in positive z-coordinate area, part of short strip and long strip
"""
cylindrical_modules = [8,13,17]
disk_modules_minus = [7,12,16]
disk_modules_plus = [9,14,18]

def distance_metric(hit):
    if hit.volume_id in cylindrical_modules:
        return np.sqrt(hit.x**2 + hit.y**2)
    else:
        return hit.z #np.absolute(hit.z)


def sort_layers(hits):

    sequence = []

    volumes = hits.volume_id.unique()
    for volume in volumes:
        volume_hits = hits[hits.volume_id == volume]
        layers = volume_hits.layer_id.unique()
        for layer in layers:
            layer_hits = volume_hits[volume_hits.layer_id == layer]
            distance = distance_metric(layer_hits.iloc[0])
            sequence.append([volume, layer, distance])
    
    sequence.sort(key=lambda x: x[2])

    return sequence