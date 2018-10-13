import numpy as np

# Padding zeros for input image to be right size
def zero_padding(img_matrix, grid_candidate):
    grid_row = grid_candidate.shape[0]
    grid_col = grid_candidate.shape[1]
    resize_row = img_matrix.shape[0]
    resize_col = img_matrix.shape[1]
    if (img_matrix.shape[0] % grid_row) != 0:
        resize_row = (img_matrix.shape[0] // grid_row + 1) * grid_row
    if (img_matrix.shape[1] % grid_col) != 0:
        resize_col = (img_matrix.shape[1] // grid_col + 1) * grid_col
    # Padding zeros
    result = np.zeros((resize_row, resize_col))
    result[:img_matrix.shape[0], :img_matrix.shape[1]] = img_matrix
    return result

# Measure the hamming distance between two grids
# Return the index for the grid of minimum hamming distance
def hamming_grid_match(grid_candidate, measure_grid):
    def hamming_dis(a, b, gray_scale=False):
        if gray_scale == False:
            xor_array = np.bitwise_xor(a, b)
            return np.count_nonzero(xor_array)
        else:
            # Calculate the sum of gray scale diff
            return np.absolute(a - b).sum()
    
    hamming_dis_list = [hamming_dis(x, measure_grid) for x in grid_candidate]
    return hamming_dis_list.index(min(hamming_dis_list))

# Only for testing
def main():
    # Test for zero padding
    # Grid matrix
    grid_candidate = np.random.rand(3, 2)
    img_matrix = np.random.rand(7, 5)
    print(img_matrix)
    print(zero_padding(img_matrix, grid_candidate))
    
    # Test for Hamming Distance
    grid_candidate = []
    candidate_one = np.array([[1, 0, 1], [1, 0, 1], [1, 0, 1]])
    candidate_two = np.array([[0, 1, 0], [0, 1, 0], [0, 0, 1]])
    measure_grid = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    grid_candidate.append(candidate_one)
    grid_candidate.append(candidate_two)
    print("Best index: ", hamming_grid_match(grid_candidate, measure_grid))
    

if __name__ == '__main__':
    main()