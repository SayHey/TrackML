import numpy as np

#Simple Coordinate Transformations

def spherical_transform(x,y,z):
    a = x**2 + y**2
    r = np.sqrt(a + z**2)
    theta = np.arctan2(z, np.sqrt(a))
    phi = np.mod(np.arctan2(y, x) + np.pi/2, np.pi) - np.pi/2
    #phi = np.arctan2(y, x)
    return r, theta, phi

def helix_transform(x,y,z):
    r = np.sqrt(x**2 + y**2 + z**2)
    x2 = x/r
    y2 = y/r
    r = np.sqrt(x**2 + y**2)
    z2 = z/r
    return x2,y2,z2

def polar_transform(x,y):
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return r, phi
