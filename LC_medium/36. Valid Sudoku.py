from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Basically we have three separate tasks: Check Rows, Check Columns, and Check All 3x3 boxes.
        I split the problem into 2 parts, firstly I check rows and cols, and later I check boxes
        created from existing rows and cols.
        """
        row_dict = defaultdict(list)
        column_dict = defaultdict(list)

        for row_index, row in enumerate(board):

            for column_index, number in enumerate(row):
                if number == ".":
                    continue

                if number in row_dict[row_index] or number in column_dict[column_index]:
                    return False
                else:
                    row_dict[row_index].append(number)
                    column_dict[column_index].append(number)

        """
        Creating boxes is daunting task. I approach it via splitting all row elements in three groups,
        that is 'for i_horizontal in range(0, 9, 3)' after that I create a for loop for extracting column
        values 'for i_vertical in range(0, 9)'. At the end we get a script that transforms 3x3 space into
        flat list, via 'len(box) == 9' used as splitter for boxes. 
        """
        sub_boxes = []
        box = []
        for i_horizontal in range(0, 9, 3):
            for i_vertical in range(0, 9):
                box += board[i_vertical][i_horizontal] + board[i_vertical][i_horizontal+1] + board[i_vertical][i_horizontal+2]
                if len(box) == 9:
                    sub_boxes.append(box)
                    box = []
        """
        Now we simply iterate through created boxes and check for duplicates similar to the row/col logic.
        """
        box_dict = defaultdict(list)
        for box_index, box in enumerate(sub_boxes):

            for number in box:
                if number == ".":
                    continue

                if number in box_dict[box_index]:
                    return False
                else:
                    box_dict[box_index].append(number)

        return True


if __name__ == "__main__":

    s = Solution()
    assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == True
    assert s.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == False
    assert s.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]) == False


"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""