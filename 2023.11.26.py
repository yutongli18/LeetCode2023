class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        num_rows, num_cols = len(mat), len(mat[0])
        if k == num_cols:
            return True
        for row_id in range(num_rows):
            sign = -1 if (row_id + 1) % 2 == 0 else 1
            for col_id in range(num_cols):
                comp_col_id = col_id + sign * k
                if comp_col_id >= num_cols:
                    comp_col_id %= num_cols
                while comp_col_id < 0:
                    comp_col_id += num_cols
                if mat[row_id][col_id] != mat[row_id][comp_col_id]:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.areSimilar(mat=[[7], [5], [5], [4], [4], [5], [8]], k=6))
