import numpy as np

# Measure the hamming distance between two grids
# Return the index for the grid of minimum hamming distance
def hamming_grid_match(grid_candidate, measure_grid):
    def hamming_dis(a, b):
        xor_array = np.bitwise_xor(a, b)
        return np.count_nonzero(xor_array)
    
    hamming_dis_list = [hamming_dis(x, measure_grid) for x in grid_candidate]
    return hamming_dis_list.index(min(hamming_dis_list))
