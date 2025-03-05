from operator import index

import numpy as np

game_matrix = np.array([[1,1,0],
                        [5,1,0],
                        [0,5,1]])

win_check_dict = {
    "rows": {"row": "",
             "winner": ""},
    "columns": {"column": "",
             "winner": ""},
    "cross":{"lr_rl": "",
             "winner": ""}
}


def check_rows_columns_cross(array):
    """
    Check if win_check = 1 - win player #1, if win_check = 2 - win player #2
    :param array:
    :return: win_check
    """
    win_check = 0
    if sum(array) == 3:
        win_check = 1
        return win_check
    elif sum(array) == 15:
        win_check = 2
        return win_check
    else:
        return win_check


def check_left_right_cross_line():
    """
    Create left right cross line
    :return: left_right array numpy with this values
    """
    left_right = np.array([])
    for data in range(3):
        left_right = np.append(arr=left_right, values=game_matrix[data, data])

    return left_right


def check_right_left_cross_line():
    """
    Create right left cross line
    :return: right_left array numpy with this values
    """
    right_left = np.array([])
    for data in range(3):
        right_left = np.append(arr=right_left, values=game_matrix[data, 2 - data])

    return right_left


# Global game check free cells
if 0 in game_matrix:
    print("Game on")
else:
    print("Game off")



# Check rows and columns
for data in range(3):
    # Rows
    row_check = check_rows_columns_cross(game_matrix[data, :])
    if row_check > 0:
        win_check_dict["rows"]["row"] = data
        win_check_dict["rows"]["winner"] = row_check
        break
    # Columns
    column_check = check_rows_columns_cross(game_matrix[:,data])
    if column_check > 0:
        win_check_dict["columns"]["column"] = data
        win_check_dict["columns"]["winner"] = column_check
        break
    # Cross Left to Right
    check_left_right = check_rows_columns_cross(check_left_right_cross_line())
    if check_left_right > 0:
        win_check_dict["cross"]["lr_rl"] = "LR"
        win_check_dict["cross"]["winner"] = check_left_right
        break
    # Cross Right to Left
    check_right_left = check_rows_columns_cross(check_right_left_cross_line())
    if check_right_left > 0:
        win_check_dict["cross"]["lr_rl"] = "RL"
        win_check_dict["cross"]["winner"] = check_right_left
        break



print(win_check_dict)