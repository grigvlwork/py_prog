printed = False


def read_sudoku():
    sudoku = list()
    for i in range(4):
        sudoku.append([int(s) for s in input().strip()])
    return sudoku


def is_solved(sudoku):
    for i in range(4):
        for j in range(4):
            if sudoku[i][j] == 0:
                return False
    return True


def square(row, column):
    if row < 2 and column < 2:
        # limits(range) for rows and columns row 0-2 col 0-2
        return [0, 2, 0, 2]
    elif row < 2 and column > 1:
        return [0, 2, 2, 4]
    elif row > 1 and column < 2:
        return [2, 4, 0, 2]
    elif row > 1 and column > 1:
        return [2, 4, 2, 4]


def possibilities(sudoku, row, column):
    nums = [1, 2, 3, 4]
    lim = square(row, column)
    for i in range(4):
        if sudoku[row][i] in nums:
            nums.remove(sudoku[row][i])
        if sudoku[i][column] in nums:
            nums.remove(sudoku[i][column])
    for x in range(lim[0], lim[1]):
        for y in range(lim[2], lim[3]):
            if sudoku[x][y] in nums:
                nums.remove(sudoku[x][y])
    return nums


def solve_sudoku(matrix):
    global printed
    if is_solved(matrix) and not printed:
        for row in matrix:
            for i in range(4):
                print(row[i], end='')
            print()
        printed = True
        return
    else:
        flag = False
        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 0:
                    nums = possibilities(matrix, i, j)
                    if len(nums) == 1:
                        matrix[i][j] = nums[0]
                        solve_sudoku(matrix)
                        flag = True
                        break
            if flag:
                break


# a = [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 0, 0], [3, 0, 0, 4]]
a = read_sudoku()
solve_sudoku(a)
