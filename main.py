from operator import index

import numpy as np

game_matrix = np.array([[1,2,8],
                        [4,5,6],
                        [7,8,9]])


# Global game check free cells
if 0 in game_matrix:
    print("Game on")
else:
    print("Game off")

# Goes through the rows and sum
for row in range(3):
    print(sum(game_matrix[row, :]))

print("===============")

# Goes through the columns and sum
for column in range(3):
    print(sum(game_matrix[ :,column]))

print("===============")

# Goes through the cross value and sum
sum_left_right = 0
sum_right_left = 0
for cross_value in range(3):
    # From left to right crosswise
    print(game_matrix[cross_value, cross_value])
    sum_left_right +=game_matrix[cross_value, cross_value]
    # From right to left crosswise
    print(game_matrix[cross_value, 2 - cross_value])
    sum_right_left += game_matrix[cross_value, 2 - cross_value]
print(sum_left_right)
print(sum_right_left)

