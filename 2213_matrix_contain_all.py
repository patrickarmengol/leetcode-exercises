
def check_matrix(matrix):
    for row in range(len(matrix)):
        if not all([len(set(matrix[row])) == len(matrix[row])]):
            return False
    for col in range(len(matrix[0])):
        col_list = [matrix[row][col] for row in range(len(matrix))]
        if not all([len(set(col_list)) == len(col_list)]):
            return False
    return True
            
def concise_check_matrix(matrix):
    return all(len(set(x)) == len(matrix) for x in matrix + list(zip(*matrix)))
            

def main():
    print(check_matrix([[1,2,3],[3,1,2],[2,3,1]]))
    print(check_matrix([[1,1,1],[1,2,3],[1,2,3]]))

    print(concise_check_matrix([[1,2,3],[3,1,2],[2,3,1]]))
    print(concise_check_matrix([[1,1,1],[1,2,3],[1,2,3]]))

if __name__ == '__main__':
    main()


"""
Runtime: 1634 ms, faster than 41.27% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
Memory Usage: 14.3 MB, less than 97.61% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.

from discussion, i found out how to invert a matrix
zip(*matrix)

so here's a one-liner:
def concise_check_matrix(matrix):
    return all(len(set(x)) == len(matrix) for x in matrix + list(zip(*matrix)))

another clean solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for row, col in zip(matrix, zip(*matrix)):
            if len(set(row)) != n or len(set(col)) != n:
                return False
        return True

an interesting sol i should look at:
def checkValid(self, matrix: List[List[int]]) -> bool:
        row, col = defaultdict(set), defaultdict(set)
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if matrix[r][c] in row[r] or matrix[r][c] in col[c]:
                    return False
                row[r].add(matrix[r][c])
                col[c].add(matrix[r][c])
        return True

"""