import numpy as np
import cython
from cython.parallel import prange

def horizontal_adjacency(grid):
    result = np.zeros((grid.shape[0], grid.shape[1]), dtype=np.uint32)
    for y in prange(grid.shape[0],nogil=True):
        span = 0
        for x in range(grid.shape[1]-1, -1, -1):
            if grid[y, x]:
                span += 1
            else:
                span = 0
            result[y, x] = span
    return result


def vertical_adjacency(grid):
    result = np.zeros((grid.shape[0], grid.shape[1]), dtype=np.uint32)
    for x in prange(grid.shape[1],nogil=True):
        span = 0
        for y in range(grid.shape[0]-1, -1, -1):
            if grid[y, x]:
                span += 1
            else:
                span = 0
            result[y, x] = span
    return result


def predict_vector_size(array):
    zero_indices = np.where(array == 0)[0]
    if len(zero_indices) == 0:
        if len(array) == 0:
            return 0
        return len(array)
    return zero_indices[0]


def h_vector(h_adjacency, x, y):
    vector_size = predict_vector_size(h_adjacency[y:, x])
    h_vector = np.zeros(vector_size, dtype=np.uint32)
    h = np.Inf
    for p in range(vector_size):
        h = np.minimum(h_adjacency[y+p, x], h)
        h_vector[p] = h
    h_vector = np.unique(h_vector)[::-1]
    return h_vector


def v_vector(v_adjacency, x, y):
    vector_size = predict_vector_size(v_adjacency[y, x:])
    v_vector = np.zeros(vector_size, dtype=np.uint32)
    v = np.Inf
    for q in range(vector_size):
        v = np.minimum(v_adjacency[y, x+q], v)
        v_vector[q] = v
    v_vector = np.unique(v_vector)[::-1]
    return v_vector


def spans(h_vector, v_vector):
    spans = np.stack((h_vector, v_vector[::-1]), axis=1)
    return spans


def biggest_span(spans):
    if len(spans) == 0:
        return np.array([0, 0], dtype=np.uint32)
    areas = spans[:, 0] * spans[:, 1]
    biggest_span_index = np.where(areas == np.amax(areas))[0][0]
    return spans[biggest_span_index]



def span_map(grid, h_adjacency, v_adjacency):

    y_values, x_values = grid.nonzero()
    span_map = np.zeros(grid.shape + (2,), dtype=np.uint32)

    for idx in prange(len(x_values),nogil=True):
        x, y = x_values[idx], y_values[idx]
        h_vec = h_vector(h_adjacency, x, y)
        v_vec = v_vector(v_adjacency, x, y)
        s = spans(h_vec, v_vec)
        s = biggest_span(s)
        span_map[y, x, :] = s

    return span_map


def biggest_span_in_span_map(span_map):
    areas = span_map[:, :, 0] * span_map[:, :, 1]
    largest_rectangle_indices = np.where(areas == np.amax(areas))
    x = largest_rectangle_indices[1][0]
    y = largest_rectangle_indices[0][0]
    span = span_map[y, x]
    return np.array([x, y, span[0], span[1]], dtype=np.uint32)
